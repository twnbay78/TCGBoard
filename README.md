# TCGBoard
A dashboard for trading card games, mainly Magic the Gathering price tracking.

## Buliding locally (Windows sadly)
The below commands produces a Windows binary executable in the "dist/" dir under the root of the project.
```
 python3 -m venv ./ -r ./requirements.txt
 ./venv/Scripts/python.exe -m PyInstaller --onefile --windowed --icon=resources/mtg_icon.ico --hidden-import=requests --paths src/ --paths ./ --paths ./.venv/ src/main.py
```