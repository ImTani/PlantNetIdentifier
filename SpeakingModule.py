import pyttsx3

def Speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
