# /home/keynine/projects/pythonRelated/WatzimaLabaree/run.py
import sys
from pathlib import Path

# Add src/ to Python path
sys.path.append(str(Path(__file__).parent / "src"))

if __name__ == "__main__":
    import uvicorn
    # Pass the app as an import string to enable reload
    uvicorn.run("watzimalabaree.main:app", host="127.0.0.1", port=8000, reload=True)
