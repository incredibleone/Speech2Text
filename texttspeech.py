import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import atexit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def intro():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("How may i help You!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning..")
        r.pause_threshold=0.5
       # r.energy_threshold=300
       # r.non_speaking_duration=0.5
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print("You said: {}\n",query)
    except Exception as e:
        print("Say it again..")
        return "None"
    
    return query




if __name__ == "__main__":
    intro()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            speak(result)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "play music" in query:
            musicDir='A:\\Music'
            songs=os.listdir(musicDir)
            os.startfile(os.path.join(musicDir,songs[0]))
        elif "time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'open code' in query:
            codePath="B:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "exit" in query:
            break
        
    