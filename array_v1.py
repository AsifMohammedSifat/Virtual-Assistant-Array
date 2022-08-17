import  speech_recognition as sr
import os
import webbrowser
from playsound import playsound
import  random

speech = sr.Recognizer()

greeting_dict = {"hello":"hello","hai":"hai","hi":"hi","array":"array"}
open_launch_dict={"open":"open",'lanuch':'launch'}
social_media_dict={"facebook":"https://www.facebook.com/","linkedin":"https://www.linkedin.com/"}

mp3_greeting_list =["F:\Projects\Asif\mp3\welcome-1.mp3"]

open_launch_list = ["F:\Projects\Asif\mp3\open_1.mp3","F:\Projects\Asif\mp3\open_2.mp3","F:\Projects\Asif\mp3\open_3.mp3"]

bye_list=["F:\Projects\Asif\mp3\gbye.mp3","F:\Projects\Asif\mp3\gthankyou_1.mp3","F:\Projects\Asif\mp3\gthankyou_2.mp3"]

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def read_voice_cmd():
    voice_text = ''
    print('Listining...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source,timeout=10,phrase_time_limit=5)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
    except sr.WaitTimeoutError:
        pass
    return voice_text

def is_valid_note(greet,voice_note):
    for key,value in greet.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except:
            pass

    return False



if __name__ == '__main__':
    playsound("F:\Projects\Asif\mp3\welcome.mp3")
    while True:
        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict,voice_note):
            print("In greeting")
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict,voice_note):
            play_sound(open_launch_list)
            if(is_valid_note(social_media_dict,voice_note)):
                key=voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
              os.system('explorer C:\\{}'.format(voice_note.replace('open ','').replace('launch ','')))
            continue
        elif 'goodbye' in voice_note:
            play_sound(bye_list)
            exit()
