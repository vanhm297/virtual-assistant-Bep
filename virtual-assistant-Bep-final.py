import speech_recognition
import pyttsx3

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

bep_brain = "Hi. I'm James. What is your name?"
bep_mouth_setting(bep_brain)
you = bep_ear_setting()
bep_brain = "Hi " + you + ", What can I help you?"
bep_mouth_setting(bep_brain)
input()


