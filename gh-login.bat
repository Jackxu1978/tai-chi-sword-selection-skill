@echo off
title GitHub CLI Login
"C:\Program Files\GitHub CLI\gh.exe" auth login --hostname github.com --git-protocol https --web
echo.
echo If you see "Authentication complete", you can close this window.
pause
