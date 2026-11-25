@echo off
title STARPath - Push to GitHub
cd /d "%~dp0"
echo ========================================================
echo   STARPath - Pushing Project Code to GitHub
echo   Repository: https://github.com/ashwinchakrawarthy-hub/starpath-co2007
echo ========================================================
echo.

"C:\Users\ELCOT\AppData\Local\Programs\MinGit\cmd\git.exe" push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! All 46 files pushed to GitHub.
    echo   View online: https://github.com/ashwinchakrawarthy-hub/starpath-co2007
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   Push encountered an error. If prompted for GitHub login,
    echo   complete the login in your browser window.
    echo ========================================================
)
echo.
pause
