#!/usr/bin/env python3

"""Text to Speech Python3 code to voice read the text file what you write in it and same the output as Mp3 format.
The code is written By Babak Emadi Nikoo"""

from gtts import gTTS
from playsound import playsound

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tts = gTTS(text=text, lang='en')
tts.save('output.mp3')
playsound('output.mp3')
