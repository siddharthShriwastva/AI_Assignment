import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from selenium import webdriver

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    """
    this function is reason for saying anything by virtual machine.
    """
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """
    this function returns the greeting according to time
    """
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        speak("Good Morning")
    elif(hour>12 and hour<3):
        speak("Good Afternoon")
    elif(hour>3 and hour<24):
        speak("Good Evening")
    speak("How may i help you?")

def take_command():
    """
    this function will take command as voice then change that to string.
    """
    ear=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        ear.pause_threshold=1  # count of seconds waiting for next word from you
        ear.energy_threshold=500 #the minimum frequency is 300 but for noiseless area if noise is more you can take more.
        audio=ear.listen(source)
    try:
        print("recognizing...")
        query=ear.recognize_google(audio,language='en-in')
        print(f"User said,{query}\n")
    except:
        print("please say that again")
        return "None"
    return query
def socialSites():
    """
    this function selects which social site you want to visit.
    """
    query=take_command().lower()
    if "twitter" in query:
        speak("opening twitter")
        driver=webdriver.Chrome(r"D:\\downloads\\chromedriver.exe")
        driver.get("https://twitter.com/login")
    elif "whatsapp" in query:
        speak("opening whatsapp")
        webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("web.whatsapp.com")
    elif "linkedin" in query:
        speak("opening linkedin")
        webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("linkedin.com")
    elif "facebook" or "fb" in query:
        speak("opening facebook")
        user="username"
        pwd="password"
        driver=webdriver.Chrome(r"D:\\downloads\\chromedriver.exe")
        driver.get("https://www.facebook.com/")
        user_find=driver.find_element_by_id("email")
        pwd_find=driver.find_element_by_id("pass")
        user_find.send_keys(user)
        pwd_find.send_keys(pwd)
        button=driver.find_element_by_id("loginbutton")
        button.submit()
        # webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("fb.com")
    else:
        speak("Sorry Sir, I don't know such social site")


if __name__=='__main__':
    speak("hello buddy! I am back");
    wishme()
    while(True):
        query=take_command().lower()
        if "how are you" in query:
            speak("Wonderful as always, thanks for asking.")

        elif "who are you" in query:
            speak("Hello, I am Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums, searching wikipedia or opening applications etcetra")

        elif "wikipedia" in query:
            speak("searching... wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("google.com")

        elif "open github" in query:
            speak("opening github")
            webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s').open("github.com")

        elif "play music" in query:
            speak("playing music")
            music_dir="D:\musics for video"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif "the time" in query:
            str_time=datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
            speak(f"sir the time is{str_time}")

        elif "open notepad" in query:
            speak("opening notepad")
            location="C:\\Users\\DELLS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(location)

        elif "open dev c++" in query:
            speak("opening Dev C++")
            location="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(location)

        elif "email" in query:
            speak("opening email")
            location="C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(location)

        elif "social site" in query:
            speak("Wow, It's very nice. with which social media site you want to connect?")
            socialSites()

        elif "thanks" in query:
            speak("You are welcome")

        elif "stop" in query:
            print("thank You.... see you soon..")
            speak("thank You.... see you soon..")

            exit()