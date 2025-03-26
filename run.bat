@echo off
REM Check if the virtual environment exists, if not, instantiate it and install dependencies (same as installer.bat)
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment exists! Creating it now...
    python -m venv venv

    if exist requirements.txt (
        echo Installing required modules.
        pip install -r requirements.txt
    ) else (
        echo No requirements.txt found.
        pause
        exit 1
    )

    call venv\Scripts\activate.bat
)

call cls
python main.py

