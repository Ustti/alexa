import speech_recognition as sr
import webbrowser 
from time import ctime
import time 
from pyautogui import * 
import time 
import random
import time
import playsound
import os
import random
from gtts import gTTS



r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexa_speak('Sorry, my speech sevice is down')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
        print(voice_data)
        if 'what is your name' in voice_data:
                alexa_speak('My name is Alexa')
        if 'what time is it' in voice_data:
                alexa_speak(ctime())
        if 'link' in voice_data:
                search = record_audio('What do you want to search for')
                url = 'www.' + search
                webbrowser.get().open(url)
                alexa_speak('Here is what I find for' + search)
        if 'search' in voice_data:
                search = record_audio('What do you want to search for')
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                alexa_speak('Here is what I find for' + search)
        if 'location' in voice_data:
                location = record_audio('What do you want to find for')
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open(url)
                print('Here is the location' + location)
        if 'code' in voice_data:
                search = record_audio('What do you want to search for')
                url = 'https://github.com/Ustti'
                webbrowser.get().open(url)
                alexa_speak('Here is what I find for' + search)
        if 'stop' in voice_data:
            time.sleep(100)
        if 'exit' in voice_data:
            exit()






time.sleep(1)
alexa_speak('How can I help u?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
