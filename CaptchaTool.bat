@echo off
color B
title CaptchaTool - By Kazkaaz
echo.

python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed.
    pause
    exit /b 1
)

python .\-\main.py
pause
exit /b 0