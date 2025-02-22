import torch
from styletts2 import StyleTTS2

# Initialize the model
model = StyleTTS2()

# Input text
text = "Hello, this is StyleTTS generating speech naturally."

# Run inference
audio = model.inference(text)

# Save the audio file
with open("output.wav", "wb") as f:
    f.write(audio)

print("✅ Speech synthesis complete! Output saved as output.wav")
