@echo off
setlocal

cd /d "%~dp0"
set DESTINATION_FOLDER=C:\Program Files (x86)\TextFortress

REM Define the source folder as the current folder
set SRC_FOLDER=%CD%\TextFortress
echo Source Folder is %SRC_FOLDER%  

echo Extracting files to %DESTINATION_FOLDER%
xcopy /E /I /Y "%SRC_FOLDER%\*" "%DESTINATION_FOLDER%"

if %errorlevel%==0 (
    echo Extraction complete.
    
    REM Change to the script directory and delete it
    pushd "%SRC_FOLDER%\TextFortress\"
    rd /S /Q .
    popd
) else (
    echo Error: Failed to copy files.
)

echo Get your file from %DESTINATION_FOLDER%
pause