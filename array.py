import speech_recognition as sr
import pyttsx3
import os


import ctypes
import os
import random
import webbrowser


speech=sr.Recognizer()

try:
    engine= pyttsx3.init()
except RuntimeError:
    print("Driver fails to initialize!!")
except ImportError:
    print("Requested Driver is not found!!")

voices=engine.getProperty("voices")

for voice in voices:
    print(voice.id)

#voice system in device
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

rate=engine.getProperty("rate")
engine.setProperty("rate",rate)

#engine.say("Hello sir..I am Asif Mohammed Sifat")
#engine.runAndWait()

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
        voice_text = ''
        print('Listining...')
        with sr.Microphone() as source:
            audio= speech.listen(source)

        try:
            voice_text = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Network Error")
        return voice_text

if __name__ == '__main__':
    #speak_text_cmd("Hello Mr. This is Asif Your Virtual Assistant.")

    while True:
        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd("Hello sir.. How can I help you?")
            continue
        elif 'open' in voice_note:
            speak_text_cmd("Opening... Sir")
            os.system('explorer C:\\{}'.format(voice_note.replace('open ','')))
            continue
        elif 'stop' in voice_note:
            speak_text_cmd("Bye Sir.. Have a nice day sir..")
            exit()


