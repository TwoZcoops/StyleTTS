import os
import sys

print("--- Diagnostic Script ---")
print(f"Current working directory: {os.getcwd()}")

# Calculate absolute paths
modules_path = os.path.abspath(os.path.join(".", "Modules"))
utils_path = os.path.abspath(os.path.join(".", "Utils"))

print(f"Calculated Modules path: {modules_path}")
print(f"Calculated Utils path: {utils_path}")

# Check if paths exist
if os.path.exists(modules_path):
    print("✅ Modules directory exists.")
else:
    print(f"❌ Modules directory NOT found at: {modules_path}")

if os.path.exists(utils_path):
    print("✅ Utils directory exists.")
else:
    print(f"❌ Utils directory NOT found at: {utils_path}")

# Check for models.py and utils.py
if os.path.exists(os.path.join(modules_path, "models.py")):
    print("✅ models.py found inside Modules.")
else:
    print(f"❌ models.py NOT found at: {os.path.join(modules_path, 'models.py')}")

if os.path.exists(os.path.join(utils_path, "utils.py")):
    print("✅ utils.py found inside Utils.")
else:
    print(f"❌ utils.py NOT found at: {os.path.join(utils_path, 'utils.py')}")
# --- sys.path modification ---

sys.path.insert(0, modules_path)
sys.path.insert(0, utils_path)

print(f"Modified sys.path: {sys.path}")

# --- Attempt Imports ---
try:
    import models
    print("✅ Successfully imported models (as a module)")
except ImportError as e:
    print(f"❌ Import Error (models): {e}")
    sys.exit(1)

try:
    from models import StyleTTS2  # Try importing something *specific*
    print("✅ Successfully imported StyleTTS2 from models")
except ImportError as e:
    print(f"❌ Import Error (StyleTTS2): {e}")
    sys.exit(1)
try:
    import utils
    print("✅ Successfully imported utils (as a module)")
except ImportError as e:
    print(f"❌ Import Error (models): {e}")
    sys.exit(1)

try:
    from utils import get_configs_of
    print("✅ Successfully imported get_configs_of from utils")
except ImportError as e:
    print(f"❌ Import Error (get_configs_of): {e}")
    sys.exit(1)

print("✅ All import checks passed (from test.py)!")