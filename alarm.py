import pyttsx3

def announcement(announcement):
    engine = pyttsx3.init()
    engine.say(announcement)
    engine.runAndWait()
