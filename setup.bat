@echo off
cls

echo Would you like to install all required python packages?
pause

cls

echo Installing packages from requirements.txt...

pip install -r requirements.txt

cls

echo Setup complete!
echo Would you like to run the bot?
pause

start.bat
pause