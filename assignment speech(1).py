import speech_recognition as sr
import datetime
import webbrowser
import time
import playsound
import os
import wikipedia
import random
from time import ctime
from gtts import gTTS
def wishME():
    hour = int (datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        joo_speak("good moring my dear")

    if hour>= 12 and hour<23:
        joo_speak("good evening my dear")
r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:   
        if ask:
            joo_speak(ask)
        audio = r.listen(source)
        voice_data = ''

       

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:  
            joo_speak('Sorry, I did not get that,can you talk again')
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
        joo_speak('My name is joo')

    if 'nice name' in voice_data:
        joo_speak('how can i help you?')

    if 'what time is it' in voice_data:
        joo_speak(ctime())
   
    if 'YouTube' in voice_data:
        webbrowser.open('https://www.youtube.com/')

    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        joo_speak('here is the location of ' + location)
                        
    if 'please search' in voice_data:
        joo_speak('Searching Wikipedia...')
        voice_data = record_audio('what do you want to search')
        voice_data = voice_data.replace("wikipedia", "")
        results = wikipedia.summary(voice_data, sentences = 3)
        joo_speak("According to Wikipedia")
        print(results)
        joo_speak(results)
    
       
    if 'thank you by' in voice_data:
        joo_speak('bye sir')
        exit()
    

  
time.sleep(1)
joo_speak('HELLO')
while 1:  
    voice_data = record_audio()
    respond(voice_data)