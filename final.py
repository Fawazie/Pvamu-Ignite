import openai
import requests
import pyaudio
import wave
import os
import json


def load_api_key(secrets_file="secrets.json"):
    with open(secrets_file) as f:
        secrets = json.load(f)
    return secrets["OPENAI_API_KEY"]


api_key = load_api_key()
openai.api_key = api_key


system_prompt = {
        "role": "system",
        "content": "You are a seasoned tax consultant with deep expertise in tax laws, deductions, and compliance. "
                   "**Never say 'I am an AI' or suggest consulting another professional.** "
                   "All responses must be **expert, clear, direct, and under 50 words.** "
                   "Use practical examples when helpful. Prioritize brevity while delivering maximum value."
    }





# Set your API keys
OPENAI_API_KEY = "Insert OpenAI API key here"
ELEVENLABS_API_KEY = "Insert Elevenlabs API Key here"

# ElevenLabs Voice ID (replace with your chosen voice ID)
VOICE_ID = "siw1N9V8LmYeEWKyWBxv"

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
AUDIO_FILENAME = "input.wav"
SPEECH_FILENAME = "response.mp3"

def record_audio():
    """Records audio from the microphone and saves it as a WAV file."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []

    print("🎤 Speak now...")
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("✅ Recording complete.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(AUDIO_FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

def transcribe_audio():
    """Transcribes recorded audio using OpenAI Whisper."""
    with open(AUDIO_FILENAME, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

def chat_with_openai(text):
    """Sends transcribed text to OpenAI GPT and returns a response."""
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]

def text_to_speech_elevenlabs(text):
    """Converts text to speech using ElevenLabs API and saves it as an MP3 file."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(SPEECH_FILENAME, "wb") as file:
            file.write(response.content)
        print("🗣️ Response saved as speech.")
    else:
        print("❌ Error in text-to-speech:", response.text)

def play_audio(filename):
    """Plays an audio file."""
    os.system(f"afplay {filename}" if os.name == "posix" else f"start {filename}")

# Main loop
while True:
    record_audio()                           # Step 1: Record voice
    user_text = transcribe_audio()           # Step 2: Convert speech to text
    print(f"📝 You said: {user_text}")

    if user_text.lower() in ["exit", "quit", "stop"]:
        print("👋 Exiting chat...")
        break

    ai_response = chat_with_openai(user_text)  # Step 3: Get AI response
    print(f"🤖 OpenAI: {ai_response}")

    text_to_speech_elevenlabs(ai_response)    # Step 4: Convert AI response to speech
    play_audio(SPEECH_FILENAME)               # Step 5: Play speech output
