import speech_recognition as sr
import pyttsx3
import webbrowser

# get the engine 
engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()
isQuit = False
while True: 
    # obtain the micro audio
    with sr.Microphone() as mic:
        print("Say something!")
        # noise cancel
        r.adjust_for_ambient_noise(mic)
        # get audio from microphone
        audio = r.listen(mic)

    text = ""
    try:
        # Use Google AI to transcribe from voice to text
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
   

    print(f"...{text}...")
    text = text.lower()
    # AI Helper is from here
    if "hello" in text:
        res = "hello Kha Nguyen"
    # escape the program
    elif "bye" in text:
        res = "bye bye Kha Nguyen"
        isQuit = True
    # open youtube search
    elif "youtube" in text :
       text = text.replace('youtube','')
       webbrowser.open_new(f"https://www.youtube.com/results?search_query={text.replace(' ','+')}")
       res = f"youtube open and search for {text}"
    # open amazon search
    elif "amazon" in text :
       text = text.replace('amazon','')
       webbrowser.open_new(f"https://www.amazon.com/s?k={text.replace(' ','+')}")
       res = f"amazon open and search for {text}"
    # do nothing for empty string
    elif text == "":
       continue 
    # Every else google search
    else:
       webbrowser.open_new(f"https://www.google.com/search?q={text.replace(' ','+')}")
       res = f"google open and search for {text}"

        
    #Response answer
    engine.say(res)
    engine.runAndWait()
    if (isQuit):
        break


