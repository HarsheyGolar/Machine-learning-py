import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import time
import datetime
import openai
import os
import subprocess
import pyaudio
import pygame
import wikipedia
from pyttsx3 import Engine, speak



#Text to Speech Engine setup......
engine=pyttsx3.init()
engine.setProperty('rate',180)
engine.setProperty('volume',1.0)

#Audio to speak introduction by jarvis official ......
def play_audio(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()


#listen to  voice command......
def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with sr.Microphone() as source:
        # r.pause_thresholds = 0.6
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"you said:{query}")
        return query.lower()
    except Exception as e:
        return"some error occured ,sorry from jarvis"


#function that helps AI to speak......
def speak(text):
    engine = pyttsx3.init(driverName="sapi5") #for windows
    engine.say(text)
    engine.runAndWait()

#Execute commands
def execute(command):
    if "open youtube" in command:
        speak("Opening Youtube sir.....")
        webbrowser.open("https://www.youtube.com")
    if "open google" in command:
        speak("Opening Google sir.....")
        webbrowser.open("https://www.google.com")
    if "play music" in command:
        speak("playing music sir....")


#main loop
if __name__=="__main__":
    play_audio("D:\Downloads\jarvis_introduction.mp3")
    while True:
        user_command = listen()
        if user_command:
            execute(user_command)

            #say(query)


