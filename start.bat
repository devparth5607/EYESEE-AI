@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "EYESEE-AI Backend" py -3 server.py
) else (
  start "EYESEE-AI Backend" python server.py
)
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8788/
