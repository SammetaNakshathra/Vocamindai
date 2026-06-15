# VocaMind AI 🎤🤖🔊

VocaMind AI is an end-to-end conversational voice assistant that enables natural voice-based interaction using modern Generative AI technologies. The system captures spoken user input, converts speech into text, processes the query using a Large Language Model (LLM), and generates a realistic voice response in real time.

The project was built to demonstrate the complete Voice AI pipeline used in modern conversational systems such as AI assistants, customer support bots, and voice-enabled applications.

VocaMind AI integrates Speech Recognition, Prompt Engineering, Generative AI, and Text-to-Speech synthesis into a single interactive web application.


# 🚀 Features

- 🎤 Real-time voice input through microphone
- 📝 Speech-to-Text transcription using OpenAI Whisper
- 🤖 Intelligent conversational responses using Groq LLMs (Llama 3.1)
- 🔊 Natural AI-generated speech using ElevenLabs
- 🌐 Interactive browser-based interface using Gradio
- ⚡ Fast inference and low response latency
- 🧠 Prompt-engineered concise conversational responses
- ☁️ Deployable as a permanent public web application using Hugging Face Spaces

# 🧠 How It Works

The application follows a multi-stage AI pipeline:

1. The user speaks into the microphone.
2. OpenAI Whisper transcribes the speech into text.
3. The transcribed text is sent to a Groq-hosted Llama 3.1 model.
4. The LLM generates a concise conversational response.
5. ElevenLabs converts the generated response into realistic speech audio.
6. The final voice response is played back to the user through the web interface.


# 📂 System Architecture

```text
User Voice Input
        ↓
OpenAI Whisper (Speech-to-Text)
        ↓
Groq LLM (Llama 3.1 Response Generation)
        ↓
ElevenLabs (Text-to-Speech)
        ↓
Voice Response Output
