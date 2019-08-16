#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
from playsound import playsound
from mpyg321.mpyg321 import MPyg321Player
from pygame import mixer

def speaker(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

while(True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Speak Anything :')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            if ('time' in format(text)):
                speaker(current_time)
                print ('Current Time =', current_time)
            elif (format(text)=='good morning'):
                speaker('A very good  morning, have a nice day')
                print ('A very good  morning, have a nice day')
            elif ('song' in format(text)):
                mixer.init()
                mixer.music.load('C:/Users/eshwar/Documents/python_tests/patience.mp3')
                mixer.music.play()
            else:
                mixer.music.stop()
        except:
            print ('Sorry could not recognize your voice')
