import os
import sys
import random
import yaml
from munch import Munch
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import torchaudio
import librosa
from nltk.tokenize import word_tokenize

# --- Section 1: Directory Check and Adjustment ---

print(f"Current working directory: {os.getcwd()}")

# Adjust this line as needed based on the output of getcwd()
os.chdir("Demo")  # Or "StyleTTS/Demo", or the full path

print(f"New working directory: {os.getcwd()}")

# --- Section 2: Add Demo to sys.path (TEMPORARY) ---
sys.path.append(os.getcwd())  # Add current (Demo) directory

# --- Section 3: Imports that Depend on the Working Directory ---
try:
    from models import *
    from utils import *
    print("✅ Successfully imported models and utils!")
except ImportError as e:
    print(f"❌ Import Error: {e}")
    sys.exit(1)  # Exit if imports fail

# --- Section 4: eSpeak NG Check ---

try:
    from phonemizer.backend import EspeakBackend
    backend = EspeakBackend("en-us")
    print("✅ eSpeak is properly detected by Phonemizer!")
except Exception as e:
    print(f"❌ eSpeak detection failed: {e}")
    sys.exit(1)

# --- Section 5: Device Check ---
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

print("✅ All preliminary checks passed!")