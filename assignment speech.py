import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import Wikipedia
import datetime
import random
from time import ctime
from gtts import gTTS
def wishME():
    hour = int (datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        joo_speak("good moring sir")

    if hour>= 12 and hour<23:
        joo_speak("good evening sir")
         
            
r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            joo_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-uk")
        except sr.UnknownValueError:
            joo_speak('Sorry, I did not get that')
        except sr.RequestError:
            joo_speak('sorry my speach service is down')
        return voice_data

def joo_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

wishME()
        
def respond(voice_data):
    if 'what is your name' in voice_data:
        joo_speak('My name is youssef and iam your voice assist')
    if 'what time now' in voice_data:
        joo_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        joo_speak('here is what I found for ' + search)
    
    if 'open download' in voice_data:
        joo_speak("opeing your download folder")
        os.startfile("C:/Users/Public/Downloads")
    if 'wikipedia' in query:
        joo_speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        joo_speak("According to Wikipedia")
        print(results)
        joo_speak(results)
        time.sleep(2)
        joo_speak("Doy Need Another Thing")


    if 'turn off' in voice_data:
        joo_speak('bye  joo ')
        exit()

time.sleep(1)

joo_speak('How can I help you?')
while 1:  
    voice_data = record_audio()
    respond(voice_data)