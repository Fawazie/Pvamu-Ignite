import openai

# Initialize OpenAI client with API key
client = openai.OpenAI(api_key="Insert OpenAI API key here")

# Define output file path
speech_file_path = "speech.mp3"

# Generate speech
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hi there, how can I help you file your taxes today?",
)

# Save the generated speech to a file
response.stream_to_file(speech_file_path)

print(f"Speech saved to {speech_file_path}")
