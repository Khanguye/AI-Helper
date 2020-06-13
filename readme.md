# How to build a simple AI helper in Python

**Summary:**
AI helper is a simple program that is built based on three simple small programs. AI helper will help you to search for content on google, youtube, amazon from voice commands.

**How to command**
Say "YouTube music 80"
Say "Amazon smartphone"
Say "local news"

**Explaination**
1. (voice2text.py)[voice2text.py]: use the speech recognition package to transcribe into text. You can follow this (https://pypi.org/project/SpeechRecognition/)[https://pypi.org/project/SpeechRecognition/] to learn more
2. (text2voice.py)[text2voice.py]: use the pyttsx3 package to convert text content to speech sound. You can follow this (https://pypi.org/project/pyttsx3/)[https://pypi.org/project/pyttsx3/]
3. (openbrowser.py)[openbrowser.py]: use the webbrowser package to open a URL on default web browser. You can follow this (https://docs.python.org/3/library/webbrowser.html)[https://docs.python.org/3/library/webbrowser.html]
4. (AI_helper.py)[AI_helper.py]: just combine three above program become an simple AI helper with voice command.


