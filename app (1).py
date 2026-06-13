import gradio as gr
import whisper
import os
from groq import Groq
from elevenlabs.client import ElevenLabs

# Load models
model = whisper.load_model("base")

# API KEYS (from Hugging Face Secrets)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tts_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# AI function
def get_ai_response(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are VocaMind AI. Reply in 1-2 short sentences."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# Text to speech
def text_to_speech(text):
    audio = tts_client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_multilingual_v2",
        text=text
    )

    file_path = "reply.mp3"
    with open(file_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    return file_path

# Full pipeline
def vocamind(audio_file):

    result = model.transcribe(audio_file)
    user_text = result["text"]

    reply_text = get_ai_response(user_text)

    audio_path = text_to_speech(reply_text)

    return user_text, reply_text, audio_path

# UI
demo = gr.Interface(
    fn=vocamind,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=[
        gr.Textbox(label="You said"),
        gr.Textbox(label="AI Reply"),
        gr.Audio(label="Voice Reply")
    ],
    title="VocaMind AI Voice Assistant"
)

demo.launch()