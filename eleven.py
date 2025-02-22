import requests

# Replace with your ElevenLabs API key
ELEVENLABS_API_KEY = "sk_102a71644f01aa954047f470a6284e38ac9266bd2516fbe3"

# Voice ID (Get from ElevenLabs API documentation or voice settings)
VOICE_ID = "eg8Q0f0fsRZA85yFiLbS"  # Example voice ID, replace with your chosen one

# Text to convert to speech
text = "And there we go! One final review from you and we will wrap up filing your taxes"
# API endpoint
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Request headers
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}

# Request payload
data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8
    }
}

# Send request
response = requests.post(url, json=data, headers=headers)

# Save response audio as an MP3 file
if response.status_code == 200:
    speech_file_path = "speech.mp3"
    with open(speech_file_path, "wb") as file:
        file.write(response.content)
    print(f"Speech saved to {speech_file_path}")
else:
    print("Error:", response.text)
