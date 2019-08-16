#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
from playsound import playsound
from mpyg321.mpyg321 import MPyg321Player
from pygame import mixer
from dict_of_songs import dict_of_songs as dos

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
            elif (format(text)=='good morning'):
                speaker('A very good  morning, have a nice day')
            elif ('play' in format(text)):
                word = format(text).lower()
                mixer.init()
                path = dos(word[5:])
                mixer.music.load(path)
                mixer.music.play()
            elif ('stop' in format(text)):
                mixer.music.stop()
        except:
            print ('Sorry could not recognize your voice')
