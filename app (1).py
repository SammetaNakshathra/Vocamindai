import gradio as gr
import whisper
import os
import asyncio
import edge_tts
from groq import Groq

# -----------------------------
# Load Whisper model
# -----------------------------
model = whisper.load_model("base")

# -----------------------------
# Load Groq API
# -----------------------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# AI Response Function
# -----------------------------
def get_ai_response(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are VocaMind AI. Reply in 1-2 short sentences."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


# -----------------------------
# Text-to-Speech using Edge-TTS
# -----------------------------
def text_to_speech(text):
    output_file = "reply.mp3"

    async def generate():
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural"
        )
        await communicate.save(output_file)

    asyncio.run(generate())

    return output_file


# -----------------------------
# Complete Voice Assistant
# -----------------------------
def vocamind(audio_file):
    if audio_file is None:
        return "No audio received.", "", None

    try:
        # Speech to Text
        result = model.transcribe(audio_file)
        user_text = result["text"].strip()

        if not user_text:
            return "Couldn't recognize speech.", "", None

        # AI Reply
        reply_text = get_ai_response(user_text)

        # Voice Reply
        audio_path = text_to_speech(reply_text)

        return user_text, reply_text, audio_path

    except Exception as e:
        return f"Error: {str(e)}", "", None


# -----------------------------
# Gradio UI
# -----------------------------
demo = gr.Interface(
    fn=vocamind,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath"
    ),
    outputs=[
        gr.Textbox(label="You said"),
        gr.Textbox(label="AI Reply"),
        gr.Audio(label="Voice Reply")
    ],
    title="🎤 VocaMind AI Voice Assistant",
    description="Speak into the microphone and get an AI voice response."
)

if __name__ == "__main__":
    demo.launch()
    
