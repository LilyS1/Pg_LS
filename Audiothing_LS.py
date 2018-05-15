import win32com.client as wncl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi Lily, what video should we watch?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    word = r.recognize_google(audio)
    speak.Speaj("Ok Lily, let's look for " + r.recognize_google(audio))

except sr.UnkownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
