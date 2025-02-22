# **🚀 Updated Setup Guide for StyleTTS (GM's VS Code & Jupyter Workspace)**  

This guide walks through **setting up StyleTTS** from scratch in **VS Code (Windows) using Conda & Jupyter Notebook** while ensuring **Phonemizer & eSpeak NG** are correctly configured.

---

## **1️⃣ Prerequisites**  

- **Git** → [Download Git](https://git-scm.com/downloads)  
- **VS Code** → [Download VS Code](https://code.visualstudio.com/)  
- **Miniconda/Anaconda** → [Download Conda](https://docs.conda.io/en/latest/miniconda.html)  
- **Jupyter Notebook** (installed via Conda)  

---

## **2️⃣ Clone the StyleTTS Repository**  

Open **VS Code**, then open a **terminal (`Ctrl + ~`)** and run:  

```sh
cd path/to/your/workspace  # Change this to your actual workspace
git clone https://github.com/TwoZcoops/StyleTTS.git
cd StyleTTS
```
This clones **your fork** of StyleTTS into your VS Code workspace.  

---

## **3️⃣ Set Up the Conda Environment**  

If you **don’t have** the **`styletts`** environment yet, create it using:  

```sh
conda env create -f environment.yml
```  

Then, **activate the environment**:  

```sh
conda activate styletts
```  

If the environment **already exists**, update it:  

```sh
conda env update --file environment.yml --prune
```

---

## **4️⃣ Install eSpeak NG (Windows Only)**  

### **🔹 Correct eSpeak NG Installation for Windows**  

1. **Download eSpeak NG** from:  
   - [📥 eSpeak NG for Windows](https://github.com/espeak-ng/espeak-ng/releases)  

2. **Run the installer** and follow the steps.  

3. **Verify installation by checking the DLL location:**  
   Open a **PowerShell terminal** and run:  
   ```powershell
   dir "C:\Program Files\eSpeak NG\*.dll"
   ```
   You should see **`libespeak-ng.dll`** in the output.

4. **Add eSpeak NG to System PATH (Required for Phonemizer)**  

   - **Press `Win + R`**, type `sysdm.cpl`, and hit **Enter**.  
   - Go to **Advanced** → Click **Environment Variables**.  
   - Under **System Variables**, find **Path** and click **Edit**.  
   - Click **New**, then add:  

     ```sh
     C:\Program Files\eSpeak NG
     ```

   - Click **OK** → **OK**.  

5. **Restart your computer OR restart your VS Code terminal**.

6. **Verify installation by running**:  

   ```sh
   espeak-ng "Hello, this is a test."
   ```
   ✅ If you hear audio output, eSpeak NG is correctly installed.

---

## **5️⃣ Fixing Phonemizer Issues (eSpeak NG Not Detected)**  

Phonemizer needs **explicit paths** for eSpeak NG.  

In Python, add:  

```python
import os
from phonemizer.backend.espeak.wrapper import EspeakWrapper

# Manually set eSpeak NG library path
os.environ["ESPEAK_LIBRARY"] = r"C:\Program Files\eSpeak NG\libespeak-ng.dll"
os.environ["ESPEAK_DATA_PATH"] = r"C:\Program Files\eSpeak NG"

# Set path explicitly in Phonemizer
EspeakWrapper.set_library(r"C:\Program Files\eSpeak NG\libespeak-ng.dll")
```

Then, **restart your Jupyter Kernel** and check Phonemizer:  

```python
import phonemizer
print(phonemizer.backend.EspeakBackend.is_available())  # Should print True
```
❌ **If it still prints `False`**, try renaming the DLL:  

```powershell
cd "C:\Program Files\eSpeak NG"
rename libespeak-ng.dll espeak-ng.dll
```
Then restart Jupyter Notebook and test again.

---

## **6️⃣ Verify Everything is Installed**  

Check if your environment has the correct packages:  

```sh
conda list
python --version  # Should match Python 3.9
which python  # Windows users: where python
```
You should see the Conda environment path (e.g., `C:\Users\YourName\anaconda3\envs\styletts\python.exe`).  

---

## **7️⃣ Download Pretrained Models**  

You **must download pretrained models** for inference.  

### **LJSpeech (Single Speaker)**  

- [📥 Model](https://huggingface.co/yl4579/StyleTTS/resolve/main/LJSpeech/Models.zip)  
- [📥 Vocoder](https://huggingface.co/yl4579/StyleTTS/resolve/main/LJSpeech/Vocoder.zip)  

### **LibriTTS (Multi-Speaker)**  

- [📥 Model](https://huggingface.co/yl4579/StyleTTS/resolve/main/LibriTTS/Models.zip)  
- [📥 Vocoder](https://huggingface.co/yl4579/StyleTTS/resolve/main/LibriTTS/Vocoder.zip)  

**Extract these files** into:  

```sh
mkdir Models Vocoder  # Windows users: If this fails, use `md Models Vocoder`
unzip Models.zip -d Models
unzip Vocoder.zip -d Vocoder
```

OR manually move the extracted files to:  

- `StyleTTS/Models/`  
- `StyleTTS/Vocoder/`  

---

## **8️⃣ Run Inference**  

Now, you can **generate speech from text**!  

### **Option 1: Using Jupyter Notebook (Recommended)**  

Start Jupyter inside your **VS Code terminal** or command prompt:  

```sh
jupyter notebook
```
This will open Jupyter Notebook in your browser.  

Open:  

- **For LJSpeech:** `Demo/Inference_LJSpeech.ipynb`  
- **For LibriTTS:** `Demo/Inference_LibriTTS.ipynb`  

Run each cell to generate speech.

#### **Real-Time Logs in Jupyter**  

To see logs while running the notebook:  

1. Open **Jupyter's main page (`localhost:8888/tree`)**.  
2. Click **"New" > "Terminal"**.  
3. Run:  

   ```sh
   conda activate styletts
   jupyter notebook
   ```

Now, the **logs will appear in the terminal** while you run the notebook.

---

### **Option 2: Using a Python Script**  

If you prefer a script, create `inference.py` and paste:  

```python
import torch
from models import *  # Load from models.py (not styletts2)

try:
    model = StyleTTS()  # Using the correct class from models.py
except NameError:
    print("❌ StyleTTS class not found in models.py. Check its name.")
    exit()

text = "Hello, this is StyleTTS generating speech naturally."
audio = model.inference(text)
with open("output.wav", "wb") as f:
    f.write(audio)
print("✅ Speech synthesis complete! Output saved as output.wav")
```

Run it:  

```sh
python inference.py
```

This generates `output.wav` with AI-generated speech.

---

## **9️⃣ Sync Your Fork with the Original Repo**  

To keep your fork **up to date**, run:  

```sh
git fetch upstream
git merge upstream/main
git push origin main
```

---

## **🎯 You're Ready to Use StyleTTS!**  

✅ Set up **VS Code workspace & Jupyter**  
✅ Installed **dependencies**  
✅ Installed **eSpeak NG & Phonemizer**  
✅ Fixed **Phonemizer detection issues**  
✅ Downloaded **pretrained models**  
✅ Ran **text-to-speech inference**  

🚀 **StyleTTS is ready to generate speech!** 🚀