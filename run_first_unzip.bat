@echo off
setlocal enabledelayedexpansion

REM Get the directory of the script
for %%F in ("%~dp0.") do set SCRIPT_DIR=%%~dpF

REM Set the name of the zip file and destination folder
set ZIP_FILE=%SCRIPT_DIR%\TextFortress_pack\TextFortress.zip
set DESTINATION_FOLDER="C:\Program Files (x86)\"

REM Check if the zip file exists
if exist "%ZIP_FILE%" (
    REM Unzip the file using PowerShell with the -Force flag
    powershell -command "Expand-Archive -Path \"%ZIP_FILE%\" -DestinationPath \"%DESTINATION_FOLDER%\" -Force"
    if %errorlevel%==0 (
        echo Zip file successfully extracted to %DESTINATION_FOLDER%.
    ) else (
        echo Error: Failed to extract the zip file.
    )

    REM Change to the script directory and delete it
    pushd "%SCRIPT_DIR%\TextFortress_pack\"
    rmdir /s /q .
    popd
) else (
    echo Error: The zip file \"%ZIP_FILE%\" does not exist.
)

REM Pause to keep the command window open
pause
