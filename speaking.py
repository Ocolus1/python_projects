import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


speak("How are you Bolu")