import pyttsx3
import datetime
# import pyaudio
# import bluetooth
import speech_recognition as sr
import http.client as httplib
import wikipedia
import webbrowser
from flask import Flask
import os
import googlesearch
from googlesearch import search
import pyautogui
import psutil
import pyjokes
from datetime import date
import random
import bluetooth
from bluetooth import *

# declaring voice of the assistance

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Reply function if there is any tasj=k which is not performend by the assistance
def reply():
    speak("O O ,I am sorry I can't do this")

# function to check internet connectivity

print("Checking your internet Connection")


def checkInternetHttplib(url="www.geeksforgeeks.org", timeout=3):
    connection = httplib.HTTPConnection(url, timeout=timeout)
    try:
        # only header requested for fast operation
        connection.request("HEAD", "/")
        connection.close()  # connection closed
        print("Internet is connected")
        return True
    except Exception as exep:
        print("Internet is not connected \nplease connect to the Internet first")
        return False


checkInternetHttplib("www.geeksforgeeks.org", 3)

# Youtube search function

def youtubesearch(term):
    output = "https://www.youtube.com/results?search_query="+term

    webbrowser.open(output)
# Google search function

def Googlesearch(query):
    output = "https://www.google.com/search?q="+query

    webbrowser.open(output)

# History of asssistance

def history(content):
    data = open("History.txt", "w")
    data.write(content)
    data.close()

# bluetooth available devices function
def bluelist():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))
    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))


# screenshot function

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\vishal sharma\\Desktop\\code\\python\\screenshot\\ss.png")

# cpu usage and battery update function

def cpu_usage():
    usage = str(psutil.cpu_percent())
    print("Cpu utilization is "+usage+"%")
    speak("Cpu utilization is"+usage+"%")
    battery = psutil.sensors_battery()
    print("Battery percentaeg is:",battery.percent)
    speak("Battery percentage is: ")
    speak(battery.percent)

# battery percentage
def battery_per():
    battery = psutil.sensors_battery()
    print("Battery percentaeg is:",battery.percent)
    speak("Battery percentage is: ",battery.percent)
    

# jokes function


def jokes():
    speak(pyjokes.get_joke())


# AGE FUNCTION AN DATE OF BIRTH TELLER

def dob():
    print("Your name is Vishal sharma ,\nYour birth date is : 15-12-2003")
    speak("Your name is Vishal sharma ,Your birth date is : 15-DECEMBER-2003")
   
# pronounce the command of user

def repeatuser(command):
    speak(command)

# Wishme function

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    if hour >= 12 and hour < 17:
        speak("Good Afternoon sir")
    if hour >= 17 and hour < 21:
        speak("Good Evening sir")
    if hour>=21 and hour <24:
        speak("Good Night sir")

# Taking command function from user

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        speak("Listning")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(f"user said: {query}")
    except Exception as e:
        print("Can you please say that again.....")
        return "None"
    return query

# main function
if __name__ == "__main__":
    wishme()
    speak("This is Memo , How may i help you")
    speak("Your last command will be saved to History")
    speak("Please select a communication medium")
    print("\nPress 1 for text typing\n")
    print("Press 2 for speak option\n")
    speak("Press one for text typing")
    speak("Press two for speak option")
    val = input("Please enter your choice : ")
    while True:
        if '1' in val:
            speak("Enabling the typing option")
            print("Only enter the lowercase letters")
            querry=input("Enter your querry here: ")
        if '2' in val:
            speak("Enabling the speaking option")
            querry = takecommand().lower()
    
        history(querry)
        if 'wikipedia' in querry:
            speak("Searching  wikipedia...")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        if 'open youtube' in querry:
            speak("Openning youtube")
            webbrowser.open("youtube.com")
            

        if 'open google' in querry:
            cont=querry.partition(' ')[2]
            speak(f"Openning {cont}")
            webbrowser.open("google.com")        
            
        if 'com' in querry:
            cont=querry.partition(' ')[2]
            speak(f"openning {cont} please wait for a while")
            Googlesearch(querry)

        if 'open Yahoo' in querry:
            cont=querry.partition(' ')[2]
            speak(f"Openning {cont}")
            webbrowser.open("Yahoo.com")
            break
      
        if 'exit' in querry:
            speak("Exiting")
            exit()

        if 'close' in querry:
            speak("Closing")
            exit()

        if 'shutdown yourself' in querry:
            speak("Closing")
            exit()

        if 'shutdown' in querry:
            speak("Shutting down")
            os.system("shutdown /s /t 1")

        if 'restart yourself' in querry:
            speak("Restarting")
            os.startfile("C:\\Users\\vishal sharma\\Desktop\\code\\python\\jarvis.py")
            exit()

        if 'restart my pc' in querry:
            speak("Restarting your pc")
            os.system("shutdown /r /t 1")

        if 'play music' in querry:
            speak("Playing music from youtube")
            webbrowser.open("https://www.youtube.com/watch?v=vX2cDW8LUWk")

        if 'play songs' in querry:
            speak("Playing songs from youtube")
            webbrowser.open("https://www.youtube.com/watch?v=vX2cDW8LUWk&list=RDvX2cDW8LUWk&start_radio=1")

        if 'what is your name' in querry:
            speak(
                "My name is no name , I am your personal assistance , i am here to help you")

        if 'who are you' in querry:
            speak("My name is memo , I am your personal assistance , i am here to help you")
            speak("I can perform some simple tasks which makes your work easy")

        if 'tell me about yourself' in querry:
            speak("My name is memo , I am your personal assistance , i am here to help you")
            speak("I can perform some simple tasks which makes your work easy")

        if 'the time' in querry:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            wishme()
            speak("The Time is ")
            speak(strtime)     

        if 'open code' in querry:
            vsPath = "C:\\Users\\vishal sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Openning..")
            os.startfile(vsPath)

        if 'open visual studio code' in querry:
            codePath = "C:\\Users\\vishal sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            cont=querry.partition(' ')[2]
            speak(f"openning {cont}")
            os.startfile(codePath)

        if 'open word' in querry:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Openning..")
            os.startfile(wordPath)
        
        if 'open excel' in querry:
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            speak("Openning..")
            os.startfile(excelPath)
        
        if 'open access' in querry:
            accessPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
            speak("Openning..")
            os.startfile(acessPath)
        
        if 'open adobe dream' in querry:
            adobePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Dreamweaver 2020.lnk"
            speak("Openning..")
            os.startfile(adobePath)
        
        if 'open android studio' in querry:
            androidPath = "C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Android Studio"
            cont=querry.partition(' ')[2]
            speak(f"openning {cont}")
            os.startfile(androidPath)
        
        if 'open adobe photoshop' in querry:
            photoPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Photoshop CC 2019.lnk"
            cont=querry.partition(' ')[2]
            speak(f"openning {cont}")
            os.startfile(photoPath)

        if 'open assassin creed rogue' in querry:
            roguePath = "D:\\Assassins Creed Rogue\\ACC.exe"
            speak("Openning..")
            os.startfile(roguePath)

        if 'open black flag' in querry:
            blackPath = "D:\\AC4BFSP RePack By Darck RePacks\\AC4BFSP.exe"
            speak("Openning ,please wait")
            os.startfile(blackPath)
        
        if 'open far cry 2' in querry:
            farPath = "D:\\Far Cry 2\\bin\\farcry2.exe"
            speak("Openning ,please wait")
            os.startfile(farPath)
        
        if 'play a game' in querry:
            roguePath = "D:\\Assassins Creed Rogue\\ACC.exe"
            blackPath = "D:\\AC4BFSP RePack By Darck RePacks\\AC4BFSP.exe"
            farPath = "D:\\Far Cry 2\\bin\\farcry2.exe"
            list1=[roguePath,farPath,blackPath]
            speak("Openning a game, please wait")
            os.startfile(random.choice(list1))
        
        if 'open a game' in querry:
            roguePath = "D:\\Assassins Creed Rogue\\ACC.exe"
            blackPath = "D:\\AC4BFSP RePack By Darck RePacks\\AC4BFSP.exe"
            farPath = "D:\\Far Cry 2\\bin\\farcry2.exe"
            list1=[roguePath,farPath,blackPath]
            speak("Openning a game, please wait")
            os.startfile(random.choice(list1))
            

        if 'open chrome' in querry:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            cont=querry.partition(' ')[2]
            speak(f"openning {cont}")
            os.startfile(chromePath)

        if 'search' in querry:
            speak("Searching on google")
            Googlesearch(querry)

        if 'who is' in querry:
            speak("Finding on google")
            Googlesearch(querry)

        if 'which' in querry:
            speak("Showing result, please wait")
            Googlesearch(querry)

        if 'how' in querry:
            Googlesearch(querry)

        if 'on youtube' in querry:
            speak("opening youtube")
            youtubesearch(querry)

        if 'screenshot' in querry:
            speak("Taking screenshot")
            screenshot()
            speak("Your screenshot was saved to the screenshot folder of my directory")

        if 'where is my screenshot' in querry:
            speak("Your screenshot was saved to the screenshot folder of my directory")

        if 'cpu usage' in querry:
            speak("Checking your cpu and battery percentage")
            cpu_usage()

        if 'battery status' in querry:
            speak("Checking battery percentage")
            battery_per()

        if 'tell me a joke' in querry:
            speak("I am telling a joke for you")
            jokes()
            speak("Ha  Ha  Ha , its soo funny")

        if 'open history file' in querry:
            filepath = "C:\\Users\\vishal sharma\\Desktop\\code\\python\\History.txt"
            cont=querry.partition(' ')[2]
            speak(f"openning {cont} please wait for a while")
            os.startfile(filepath)

        if 'birthdate' in querry:
            dob()
        
        if 'date of birth' in querry:
            dob()
        
        if 'date' in querry:
            todays_date=date.today()
            print("Today's date is: ",todays_date)
            speak(todays_date)
        
        if 'my name' in querry:
            print("Your name is vishal sharma")
            speak("Your name is vishal sharma")
        
        if '.in' in querry:
            cont=querry.partition(' ')[2]
            speak(f"openning {querry}")
            Googlesearch(querry)
        
        if 'good morning ' in querry:
            speak("Good morning")
            speak("Have a noice day dear")
            
        if 'good evening ' in querry:
            speak("Good evening")
            
        if 'good night ' in querry:
            speak("Good Night")
            speak("Sweet dreems dear")
        
        if 'i am sad' in querry:
            speak('please tell me the reason')
            takecommand()
            speak("oh dear dont be sad, go and do something exciting")
        
        if 'i love you memo' in querry:
            speak("  ")
            speak("ha ,I love you too dear")
            speak("Feeling to much love")
        
        if 'speak' in querry:
            cont=querry.partition(' ')[2]
            speak(cont)
        
        if 'repeat my words' in querry:
            repeatuser(querry)
        
        if 'list available devices' in querry:
            speak("checking for available bluetooth devices near me")
            bluelist()
            
            
        
        