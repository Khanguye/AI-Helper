import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as mic:
    print("Say something!")
    r.adjust_for_ambient_noise(mic)
    audio = r.listen(mic)

#Capture Audio and pass to google AI to transcribe
text = ""
try:
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

#Print audio text    
print(f"...{text}")
