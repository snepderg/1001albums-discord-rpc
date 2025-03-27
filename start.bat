@echo off
REM start.bat

cls
echo 1001 Albums Discord RPC Installer/Runner
echo by Snepderg
echo 1001Albums: https://1001albumsgenerator.com
timeout /t 4 /nobreak >nul
cls

if not exist "venv\Scripts\activate.bat" (
    goto install
) else (
    goto run
)

:install
echo No virtual environment exists! Creating it now...
python -m venv venv
if %errorlevel% neq 0 (
    echo Failed to create virtual environment!
    pause
    exit /b 1
)

if exist requirements.txt (
    echo Installing required modules...
    venv\Scripts\python -m pip install -r requirements.txt
) else (
    echo No requirements.txt found.
    pause
    exit /b 1
)

if not exist .env (
    echo Creating empty .env file ^for config...
    (
        echo # Your Discord Application ID. Create one here:
        echo # - https://discord.com/developers/applications
        echo DISCORD_ACTIVITY_TOKEN=
        echo # Your 1001 Albums Project ID. Create one here:
        echo # (Summary ID is recommended for security)
        echo # - https://1001albumsgenerator.com
        echo PROJECT_ID=
        echo # How many seconds between updates. ^If left blank will default to 300.
        echo UPDATE_INTERVAL=
    ) > .env
) else (
    echo .env file already exists in directory.
)

cls
echo Installation completed.
echo Note: You will need to fill out the .env credentials for the script to function.
echo Have fun! ~ Snep
timeout /t 5 /nobreak >nul
cls
goto run

:run
echo Running RPC...
venv\Scripts\python main.py
