@echo off
setlocal enabledelayedexpansion

REM Check if Python is already installed
where python >nul 2>nul
if %errorlevel%==0 (
    for /f "delims=" %%v in ('python -V 2^>^&1') do set current_version=%%v
    echo Python is already installed with version !current_version!.
) else (
    echo Python is not installed.
    echo Please install Python and add it to the system PATH with the given Python 3.11.5 installer.
)

REM Pause to keep the command window open
pause
