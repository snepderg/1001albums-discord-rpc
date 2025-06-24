@echo off
REM Delay to allow system and services to settle.

title 1001AlbumsRPC
color 0B

timeout /t 30 >nul

REM Always run from script's own directory
cd /d %~dp0

call venv\Scripts\python main.py