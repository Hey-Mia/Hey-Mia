import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
from datetime import datetime
import os
import pyjokes


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 250)

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Aktualne Posloucham okoli..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Vyhodnocovani")   
        query = r.recognize_google(audio, language ='en-in')
        print("Ty jsi Rekl: " + query)
  
    except Exception as e:
        print(e)
        print("Zadny zvuk nebyl zaznamenan, opakuji znovu..") 
        return "None"
     
    return query

loop1 = True
while loop1==True:
    command = takeCommand()
    if "hey Mia" in command:
        speak("Yes?")
        while True:
            command = takeCommand()
            #Conversational
            if 'how are you' in command:
                speak("I'm doing well")
            if 'thank you' in command:
                speak("No problem.")

            #Tasks
            if 'play' in command:
                song = command.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
            if 'joke' in command:
                speak(pyjokes.get_joke())
            if 'time' in command:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                speak("The Current Time is " + current_time)  
            if 'random number' in command:
                randInt = random.randint(0, 10) 
                speak("A random number between 0 and 10 is " + str(randInt))
            if 'open slack' in command:
                os.system('open /Applications/Slack.app')
                speak("Opening Slack")
            if 'close slack' in command:
                os.system('open /Applications/Slack.app')
                speak("Closing Slack")

    else:
        continue