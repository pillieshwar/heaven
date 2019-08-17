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
from dict_of_bdays import dict_of_bdays as bday
from voice_modulator import voice_modulator as vm
from datetime import date
import time


def speaker(text):
    vm(text)

while(True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Speak Anything :')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            now = datetime.now()
            current_time = now.strftime("%I:%M")
            if ('time' in format(text)):
                speaker(current_time)
                print ('Current Time =', current_time)
            elif (format(text)=='good morning'):
                speaker('A very good  morning BOSS, have a nice day')
            elif ('play' in format(text)):
                word = format(text).lower()
                print (word[5:])
                mixer.init()
                path = dos(word[5:])
                mixer.music.load(path)
                mixer.music.play()
            elif ('stop' in format(text)):
                print ('music stopped')
                mixer.music.stop()
            elif ('birthdays' in format(text)):
                print (format(text))
                msg = bday()
                speaker(msg)
        except:
            print ('Sorry could not recognize your voice')
