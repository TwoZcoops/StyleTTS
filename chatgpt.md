Your log output shows that several steps are working fine (changing directories, loading packages, setting up your mel transform, etc.), but there are a few key issues causing errors in your workflow:

1. **Phonemizer Initialization Error:**  
   In cell 7, when trying to create the global phonemizer with  
   ```python
   global_phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True, with_stress=True)
   ```  
   you get a `RuntimeError: espeak not installed on your system`. This error means that phonemizer’s ESpeak backend isn’t detecting a valid eSpeak-ng installation. To resolve this:
   - **Ensure eSpeak-ng is correctly installed:** Verify that you have the x64 version installed.  
   - **Set the library path explicitly:**  
     Before any phonemizer imports, add:  
     ```python
     from phonemizer.backend.espeak.wrapper import EspeakWrapper
     EspeakWrapper.set_library(r"C:\Program Files\eSpeak NG\libespeak-ng.dll")
     ```  
     Also, set the executable path (if required) by setting the environment variable:  
     ```python
     import os
     os.environ["PHONEMIZER_ESPEAK_PATH"] = r"C:\Program Files\eSpeak NG\espeak-ng.exe"
     ```  
   - **Restart your kernel/terminal** so these changes are recognized.

2. **Missing Module "attrdict":**  
   In cell 8, you encounter `ModuleNotFoundError: No module named 'attrdict'`. This is solved by installing the module:
   ```bash
   pip install attrdict
   ```

3. **FileNotFoundError for LibriTTS Config:**  
   In cell 9, the error indicates that `./Models/LibriTTS/config.yml` cannot be found. Make sure you have downloaded and unzipped the pretrained LibriTTS models into a folder named `Models/LibriTTS` inside your repository. If you intended to run the LJSpeech demo instead, adjust your paths accordingly.

4. **Subsequent Cascading Errors:**  
   Cells 10, 12, 13, and 17–18 fail because they depend on earlier cells (like cell 7 for `global_phonemizer` and cell 9 for `config`) that didn’t execute successfully. Once you fix the phonemizer initialization and ensure your model files are in the correct location, those errors should resolve.

5. **Test-Clean Path Issue (Cell 15):**  
   The error here (`FileNotFoundError`) indicates that the specified test-clean directory does not exist on your system. Verify the path or skip this step if you’re not using LibriTTS test data.

**Next Steps:**  
- Fix the eSpeak-ng detection by explicitly setting the library path (and executable path if needed) and restarting your kernel.  
- Install any missing modules (like `attrdict`).  
- Confirm that your pretrained model files (config.yml, checkpoint files) are correctly placed in the expected directories.  
- Re-run the cells in order, as many of the later errors depend on successful execution of earlier cells.

Once these issues are addressed, you should be able to run the inference demo as intended.

Let me know if you need further help! 

  
—  
References:  
citeturn1search3  
citeturn1search1