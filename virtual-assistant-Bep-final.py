import speech_recognition
import pyttsx3
import random
from datetime import date

#bep brain
bep_brain = ""

#speech recognition function
bep_ear = speech_recognition.Recognizer()
def bep_ear_setting():
    with speech_recognition.Microphone() as mic:
        audio = bep_ear.listen(mic, timeout = 5, phrase_time_limit = 5)
    you = bep_ear.recognize_google(audio)
    print(you)
    return you

#text to speech function
bep_mouth = pyttsx3.init()
def bep_mouth_setting(bep_brain):
    print(bep_brain)
    bep_mouth.say(bep_brain)
    bep_mouth.runAndWait()


#recommend a taylor swift song
def recommend_TS_song():
    if "happy" in you:
        with open('TS-happy-songs.txt','r') as file:
            happySong = file.read().split("\n*")
        song_Recommend = str(random.choice(happySong))
    elif "sad" in you:
        with open('TS-sad-songs.txt','r') as file:
            sadSong = file.read().split("\n*")
        song_Recommend = str(random.choice(sadSong))
    else:
        bep_mouth_setting("Sorry I can't help you this time")
    bep_mouth_setting(song_Recommend)


#intro
bep_brain = "Hi. I'm James. What is your name?"
bep_mouth_setting(bep_brain)
you = bep_ear_setting()

bep_brain = "Hi " + you + ", What can I help you?"
bep_mouth_setting(bep_brain)
you = bep_ear_setting()

#Functions
if "today" in you:
    today = date.today()
    d2 = today.strftime("Today is %B %d, %Y")
    bep_mouth_setting(d2)

if "song" in you:
    bep_mouth_setting("a Happy or a Sad song?")
    you = bep_ear_setting()
    recommend_TS_song()

else:
    bep_mouth_setting("Sorry I can't hear you. Say again")
    you = bep_ear_setting()
    
    

input()
