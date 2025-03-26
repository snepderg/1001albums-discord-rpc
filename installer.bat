@echo off
REM Create virtual environment
python -m venv venv

if exist "venv\Scripts\activate.bat" (
    echo Virtual environment already exists in this directory, exiting...
    pause
    exit 0
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies from requirements.txt (if it exists)
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo No requirements.txt found.
    pause
    exit 1
)
