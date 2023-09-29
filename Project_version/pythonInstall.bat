@echo off
setlocal enabledelayedexpansion

REM Check if Python is already installed
where python >nul 2>nul
if %errorlevel%==0 (
    for /f "delims=" %%v in ('python -V 2^>^&1') do set current_version=%%v
    echo Python is already installed with version !current_version!.
) else (
    REM Set the Python version you want to install
    set PYTHON_VERSION=3.11.5

    REM Set the download URL for the Python installer
    set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

    REM Set the installation directory
    set INSTALL_DIR=C:\Python%PYTHON_VERSION%

    REM Download the Python installer
    echo Downloading Python %PYTHON_VERSION%...
    curl -o python_installer.exe %PYTHON_URL%

    REM Install Python silently
    echo Installing Python %PYTHON_VERSION%...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=0 Include_test=0 Include_tcltk=0 Include_doc=0

    REM Add Python to the PATH
    setx PATH "%INSTALL_DIR%;%PATH%"

    REM Clean up the installer
    del python_installer.exe

    echo Python %PYTHON_VERSION% has been installed to %INSTALL_DIR% and added to the PATH.
)

REM Pause to keep the command window open
pause
