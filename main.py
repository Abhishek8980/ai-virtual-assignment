import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import mtranslate



engine = pyttsx3.init()
voices = engine.getProperty('voices')       # getting details of current voice

engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content =  r.recognize_google(audio,language="en-in")
            print("you said.......... " + content)
        except Exception as e:
            print("please try again...")

    return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome , How can i help you.")
        elif "play music" in request:
            speak("playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=sZrTJesvJeo&list=RDsZrTJesvJeo&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=XO8wew38VM8&list=RDXO8wew38VM8&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=JgDNFQ2RaLQ&list=RDXO8wew38VM8&index=4")

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is" + str(now_time))

        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is" + str(now_time))
        
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task :" + task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt" , "r") as file:
                speak("Work we have to do today is : " + file.read())
        elif "so work" in request:
            with open ("todo.txt" , "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            )

        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")

        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            speak("opening" + query)      #may be need to remove


        elif "tell me" in request:
            request = request.replace("jarvis", "")
            request = request.replace("tell me", "")
            print(request) # also you remove
            result = wikipedia.summary(request, sentences=2)
            print(result) #also you remove
            speak(result)

        elif "search" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search about", "")
            webbrowser.open("https://www.google.com/search?q="+request)
            speak(request)


        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+918120745489", "Hi , how are you ", 2, 24,30)




main_process()