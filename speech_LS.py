import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's poppin'?")

answer = pg.prompt("Enter you mood below")

if answer == "happy":
    speak.Speak("congratumalations")

elif answer == "sad":
    speak.Speak("that's cool")

elif answer == "quite content":
    speak.Speak("glad to hear")

elif answer == "anxious":
    speak.Speak("don't worry hun....................you're gonna slay whatever you're worrying about")

elif answer == "like beyonce":
    speak.Speak("get it boo")

elif answer == "cool":
    speak.Speak("then you should probs get a sweatshirt")

elif answer == "tired":
    speak.Speak("wakey wakey")

speak.Speak("What videos do you want to watch?")

video = pg.prompt("Enter video below.")

speak.Speak("Ok, let's go look for some " + video + " on YouTube")

wb.open("https://www.youtube.com/results?search_query=" + video)
