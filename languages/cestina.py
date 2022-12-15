import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
from datetime import datetime
import os

cz_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', cz_voice_id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Deciphering")   
        query = r.recognize_google(audio, language ='cs-CZ')
        print("You Said: " + query)
  
    except Exception as e:
        print(e)
        print("Did not hear anything") 
        return "None"
     
    return query


while True:
    command = takeCommand()
    #Conversational
    if 'Jak se máš?' in command:
        speak("Mám se dobře")
    if 'thank you' in command:
        speak("Anytime")

    #Tasks
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
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