import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi Lily, what would you like to search for today?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Lily, let's look for " + r.recognize_google(audio) + " on Google")
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnkownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print ("Could not request results from Google Speech Recognitiob sercice; {0}".format(e))
