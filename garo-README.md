# **🚀 Optimized Setup Guide for StyleTTS (VS Code & Jupyter)**

This guide provides a **step-by-step walkthrough** to set up **StyleTTS in VS Code on Windows** using **Conda & Jupyter Notebook**, while ensuring **Phonemizer & eSpeak NG** are correctly configured.

---

## **1️⃣ Prerequisites**

Before starting, make sure you have the following installed:

- ✅ **Git** → [Download Git](https://git-scm.com/downloads)
- ✅ **VS Code** → [Download VS Code](https://code.visualstudio.com/)
- ✅ **Miniconda/Anaconda** → [Download Conda](https://docs.conda.io/en/latest/miniconda.html)
- ✅ **Jupyter Notebook** (installed via Conda)
- ✅ **Git LFS (Large File Storage)** → Install with:

  ```sh
  git lfs install
  ```

---

## **2️⃣ Clone the StyleTTS Repository**

1. **Fork the repository** on GitHub:  
   - Go to [https://github.com/yl4579/StyleTTS](https://github.com/yl4579/StyleTTS) and click **Fork**.
2. **Clone your fork** in VS Code:

   ```sh
   cd path/to/your/workspace  # Change to your workspace
   git clone https://github.com/TwoZcoops/StyleTTS.git
   cd StyleTTS
   ```

---

## **3️⃣ Set Up Git LFS Before Doing Anything Else**

Since `.pth` model files **should not** be committed to Git, set up Git LFS immediately:

```sh
git lfs install
git lfs track "Models/LJSpeech/*.pth"
git lfs track "Vocoder/g_*"
git lfs track "Utils/ASR/epoch_*.pth"
git add .gitattributes
git commit -m "Set up Git LFS for model files"
```

---

## **4️⃣ Configure Upstream Remote (For Syncing Updates)**

Ensure your fork is set to track the **original repo**:

```sh
git remote add upstream https://github.com/yl4579/StyleTTS.git
git fetch upstream
git merge upstream/main
```

✅ To **sync updates later**, run:

```sh
git fetch upstream
git merge upstream/main
git push origin main
```

---

## **5️⃣ Create & Activate the Conda Environment**

If you don’t already have the **`styletts`** environment, create it:

```sh
conda env create -f environment.yml
```

Then activate:

```sh
conda activate styletts
```

To update later:

```sh
conda env update --file environment.yml --prune
```

---

## **6️⃣ Install eSpeak NG (Windows Only)**

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
4. **Manually Add eSpeak NG to System PATH (Required for Phonemizer)**
   - **Press `Win + R`**, type `sysdm.cpl`, and hit **Enter**.
   - Go to **Advanced** → Click **Environment Variables**.
   - Under **System Variables**, find **Path** and click **Edit**.
   - Click **New**, then add:

     ```sh
     C:\Program Files\eSpeak NG
     ```

   - Click **OK** → **OK**.
5. **Restart your computer OR restart your VS Code terminal.**
6. **Verify installation by running:**

   ```sh
   espeak-ng "Hello, this is a test."
   ```

   ✅ If you hear audio output, eSpeak NG is correctly installed.

---

## **7️⃣ Ensure VS Code Loads eSpeak NG Correctly**

Since VS Code sometimes **does not inherit environment variables**, update your **VS Code `settings.json`**:

1. Open **VS Code**.
2. Press **`Ctrl + Shift + P`** → Type `"Preferences: Open User Settings (JSON)"` → Select it.
3. Inside the `"windows"` section, add:

   ```json
   "terminal.integrated.env.windows": {
       "PHONEMIZER_ESPEAK_LIBRARY": "C:\\Program Files\\eSpeak NG\\libespeak-ng.dll",
       "ESPEAK_DATA_PATH": "C:\\Program Files\\eSpeak NG\\espeak-ng-data",
       "PHONEMIZER_ESPEAK_PATH": "C:\\Program Files\\eSpeak NG\\espeak-ng.exe"
   }
   ```

4. **Save the file (`Ctrl + S`)**.
5. **Restart VS Code completely**.

---

## **8️⃣ Verify Phonemizer Works with eSpeak NG**

Run this Python script inside your **styletts** Conda environment:

```python
from phonemizer import phonemize

text = "Hello, world!"
phonemes = phonemize(text, language='en-us', backend='espeak')
print("Phonemized Output:", phonemes)
```

✅ **Expected Output:**

```text
Phonemized Output: həlˈoʊ wɝːld
```

---

## **9️⃣ Run Inference with StyleTTS**

### **Option 1: Using Jupyter Notebook (Recommended)**

```sh
jupyter notebook
```

- Open **`Demo/Inference_LJSpeech.ipynb`** and run the cells.

---

### **Option 2: Using a Python Script**

Create a file (e.g., `inference.py`) with:

```python
import torch
from models import *

model = StyleTTS()
text = "Hello, this is StyleTTS generating speech naturally."
audio = model.inference(text)

with open("output.wav", "wb") as f:
    f.write(audio)

print("✅ Speech synthesis complete! Output saved as output.wav")
```

Then run it:

```sh
python inference.py
```

---

## **🔟 Final Sync: Keep Your Fork Up-to-Date**

```sh
git fetch upstream
git merge upstream/main
git push origin main
```

---

## **🎯 Final Checklist**

- ✅ **Fixed VS Code environment variable issues**
- ✅ **Verified Phonemizer works with eSpeak NG**
- ✅ **Ran text-to-speech inference successfully**

🚀 **StyleTTS is now fully set up and ready to use!** 🚀

---

## **🔹 Optimized `.gitignore`**

```gitignore
# Ignore compiled Python files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore model checkpoint files
Models/LJSpeech/
Vocoder/g_*
Utils/ASR/epoch_*.pth
