import torch
from models import *  # Load all functions from models.py
from utils import *  # Load utilities

# Initialize StyleTTS model (check models.py for correct class name)
try:
    model = StyleTTS()  # If this fails, check models.py for actual class
except NameError:
    print("❌ StyleTTS class not found in models.py. Check its name.")
    exit()

# Input text
text = "Hello, this is StyleTTS generating speech naturally."

# Run inference
audio = model.inference(text)

# Save the output
with open("output.wav", "wb") as f:
    f.write(audio)

print("✅ Speech synthesis complete! Output saved as output.wav")
