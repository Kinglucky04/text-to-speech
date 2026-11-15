import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            unanimous_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            unanimous_speak("Sorry, I didn't understand that")
        except sr.RequestError:
            unanimous_speak("Sorry, my speech service is down")
        return voice_data

def response(voice_data):
    if "what is your name" in voice_data:
        unanimous_speak("my name is Unanimous")
    if "what time is it" in voice_data:
        unanimous_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("what do you want to search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        unanimous_speak("this is what i found for " + search)
    if 'find location' in voice_data:
            location = record_audio("which location do you want to find?")
            url = "https://google.nl/maps/place/" + location
            webbrowser.get().open(url)
            unanimous_speak("this is what i found for " + location)
    if 'exit' in voice_data:
        exit()


def unanimous_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


print("how can i help you?") 
time.sleep(1)
while 1:
    voice_data = record_audio()
    response(voice_data)
