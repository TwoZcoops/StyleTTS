# **🚀 Setup Guide for StyleTTS (GM's VS Code Workspace)**

This guide walks through **setting up StyleTTS** from scratch in **VS Code (Windows) using Conda**.

## **1️⃣ Prerequisites**

- **Git** → [Download Git](https://git-scm.com/downloads)
- **VS Code** → [Download VS Code](https://code.visualstudio.com/)
- **Miniconda/Anaconda** → [Download Conda](https://docs.conda.io/en/latest/miniconda.html)

---

## **2️⃣ Clone Your Fork**

Open **VS Code**, then open a **terminal (`Ctrl + ~`)** and run:

```sh
cd path/to/your/workspace  # Change this to your actual workspace
git clone https://github.com/TwoZcoops/StyleTTS.git
cd StyleTTS
```

This clones **your fork** of StyleTTS into your VS Code workspace.

---

## **3️⃣ Set Up the Conda Environment**

If you don’t have the **`styletts`** environment yet, create it using:

```sh
conda env create -f requirements.yml
```

Then, **activate the environment**:

```sh
conda activate styletts
```

If the environment **already exists**, update it:

```sh
conda env update --file requirements.yml --prune
```

---

## **4️⃣ Verify Everything is Installed**

Check if your environment has the correct packages:

```sh
conda list
python --version  # Should match Python 3.9
which python  # Windows users: where python
```

You should see the Conda environment path (e.g., `C:\Users\YourName\anaconda3\envs\styletts\python.exe`).

---

## **5️⃣ Download Pretrained Models**

You **must download pretrained models** for inference.

### **LJSpeech (Single Speaker)**

- [📥 Model](https://huggingface.co/yl4579/StyleTTS/resolve/main/LJSpeech/Models.zip)
- [📥 Vocoder](https://huggingface.co/yl4579/StyleTTS/resolve/main/LJSpeech/Vocoder.zip)

### **LibriTTS (Multi-Speaker)**

- [📥 Model](https://huggingface.co/yl4579/StyleTTS/resolve/main/LibriTTS/Models.zip)
- [📥 Vocoder](https://huggingface.co/yl4579/StyleTTS/resolve/main/LibriTTS/Vocoder.zip)

**Extract these files** into:

```sh
mkdir Models Vocoder
unzip Models.zip -d Models
unzip Vocoder.zip -d Vocoder
```

OR manually move the extracted files to:

- `StyleTTS/Models/`
- `StyleTTS/Vocoder/`

---

## **6️⃣ Run Inference**

Now, you can **generate speech from text**!

### **Option 1: Using Jupyter Notebook**

Start Jupyter:

```sh
jupyter notebook
```

Open:

- **For LJSpeech:** `Demo/Inference_LJSpeech.ipynb`
- **For LibriTTS:** `Demo/Inference_LibriTTS.ipynb`

Run each cell to generate speech.

### **Option 2: Using a Python Script**

If you prefer a script, create `inference.py` and paste:

```python
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

print("Speech synthesis complete! Output saved as output.wav")
```

Run it:

```sh
python inference.py
```

This generates `output.wav` with AI-generated speech.

---

## **7️⃣ Sync Your Fork with the Original Repo**

To keep your fork **up to date**, run:

```sh
git fetch upstream
git merge upstream/main
git push origin main
```

---

## **🎯 You're Ready to Use StyleTTS!**

✅ Set up **VS Code workspace**  
✅ Installed **dependencies**  
✅ Downloaded **pretrained models**  
✅ Ran **text-to-speech inference**
