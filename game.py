from pathlib import Path
import runpy

# Run the actual game script located in "New folder/game.py"
runpy.run_path(str(Path(__file__).resolve().parent / "New folder" / "game.py"))
