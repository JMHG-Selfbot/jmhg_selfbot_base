@echo off
title JMHG Prerequisits
color 1
echo Checking Pip Version And Installing Most UpTo Date One
python -m pip install --upgrade pip
color A
echo Installing Prerequisits The SelfBot Needs To Be Able To Run
pip install discord.py
pip install pyfiglet
pause