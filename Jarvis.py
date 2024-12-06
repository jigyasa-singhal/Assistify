import pyttsx3 #------- pip install pyttsx3, to convert text to voice 
import speech_recognition as sr    # it is for speech recognition
import datetime # for wish function
import os #for opening system apps like notepad
import cv2 # for opening camera
import sys #for exiting from the program

from cv2 import *
from requests import get # get is used in finding the ip adderss of device with help of requests module
#to send the requets to fetch the news
import requests #to send the requets to fetch the news
import webbrowser #for open the webpage of youtube
import sys  #for exiting from the program after saying no thanks
import wikipedia
import time #to use the sleep method ,for the time(1 second)
import pyautogui #used for automate the things,
# like, switch between the windows
import pyjokes #for jokes listening ,pip install pyjokes
from bs4 import BeautifulSoup #for taking the temperature data  pip install bs4
from pywikihow import search_wikihow # for how to do mode(searching the data) pip install pywikihow
import psutil #for checking the battery percentage  pip install psutil
from PIL import Image  #pillow library for opening and closing the image(screenshot or camera)


import datetime as dt

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUi import Ui_MainWindow

from win10toast import ToastNotifier  #for showing the notification


engine = pyttsx3.init('sapi5') #it provides an engine to convert the text to voic0e
# for running the speak function()
voices = engine.getProperty('voices')
# print(voices[0].id)  to print the name of voice
engine.setProperty('voices', voices[1].id)  # for name of voice[0]

# Function made to convert text to speech(audio) 
# text to speech 
def speak(audio):  #speak function define "pip install pyaudio(download with python unofficial binaries)"
    # to convert text into voice
    engine.say(audio)
    print(audio)
    engine.runAndWait()
  
  
  
def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    # speak("Installing and checking all drivers")
    # speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment...")
    # speak("All drivers are up and running")
    # speak("All systems have been activated")
    speak("Now I am online")  
  
# to wish the good morning wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt= time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12: #from 12am to untill 12 pm
        speak(f"Good Morning Sir, it's {tt}")
        print(f"Good Morning Sir, it's {tt}")
    elif hour > 12 and hour <= 17: #from 12pm to 5pm
        speak(f"Good Afternoon Sir, it's {tt}")
    elif hour>17 and hour<=20:
        speak(f"Good Evening Sir, it's {tt}")
    elif hour>20 and hour<=24:
        speak(f"Good Night Sir, it's {tt}")    
    # speak("I am Jarvis,please tell me how can i help you")
    speak("Jarvis is Here, Please tell how can i help you")
        # speak("I am ready for the work...")  
    speak("Listening mode is on...")
        # to convert voice into text
    

    
    
def notification():


                #specify the parameters
# from win10toast import ToastNotifier
  
# create an object to ToastNotifier class
    n = ToastNotifier()
    
    n.show_toast("Jarvis has been activated", "Hey, I am Jarvis, I am Online now!", duration = 2.5,
    icon_path ="C:\\Users\\yashs\\OneDrive\\Desktop\\JarvisGui\\attachment_97306422.ico") 


    # hour = int(datetime.datetime.now().hour)
    # if hour>=0 and hour<=12:
    #     speak("Good Morning")
    # elif hour>12 and hour<18:
    #     speak("Good afternoon")
    # else:
    #     speak("Good evening")
    # # c_time = obj.tell_time()
    # # speak(f"Currently it is {c_time}")
    # speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")    
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()



    def run(self):
        
        
        #  self.TaskExecution()
         
         
        speak("Please say wake up, come online, or activate now ,to run jarvis")
        
        
        while True:
            self.query =self.takecommand().lower()
            if(("wake up" in self.query) or ("get up" in self.query) or  ("online" in self.query) or  ("activate now" in self.query)):
                    self.TaskExecution()
                    
                    
            elif(("goodbye" in self.query) or ("you can go offline" in self.query) or ("you can off" in self.query) or ("you can be off" in self.query)):
                speak("Thanks for using me Sir\t, It was very nice to work for you")
                sys.exit()  
        
        
        
        
        
        
        # "THIS CODE WAS FOR JARVIS TO  BE CONTINUE IN LISTENIG MODE EVERY TIME"
        # speak("Please say wake up to run jarvis")
        # while True:
        #     self.query=self.takecommand()
        #     if(("wake up" in self.query) or ("get up jarvis" in self.query)):
        #         self.TaskExecution()
        
        
      
    
    def takecommand(self):
        try:
            
            r = sr.Recognizer()
            with sr.Microphone() as source:
                # print("Listening...")
                # speak("I am listening...")
                r.pause_threshold = 1 # if we stop for sometime,then jarvis not leave to listen us
                # timeout=5, means 5secs, 
                audio = r.listen(source, timeout=5, phrase_time_limit=8) #these 1 and all values are in seconds
            try:
                print("Recognising...")
                qquery = r.recognize_google(audio, language="en-in")
                self.query=qquery.lower()
                # print(self.query)
                # que = query.capitalize()  # for capitalize the first letter of the word
                print(f"You Said: {self.query}")  # f-string used 

            except Exception as e:
                # speak("Can't able to hear,Please Say that again")
                # speak("Please try again")
                # speak("I am listening...")
                return "none"
            # self.query=self.takecommand()
            self.query=self.query.lower()
            return self.query
            # return self.query
        except:
            # print(e)
            return False    

    def TaskExecution(self):
        startup()
        notification()
        wish()
        
        
        
        if(('hello jarvis' in self.query) or ('hey jarvis' in self.query) or ('hi jarvis' in self.query)):
                speak("Hello Sir")
                # speak("How are you!")
                self.query=self.takecommand().lower()
                
        elif(('i am fine' in self.query) or ('i am good' in self.query)or ('i am also good' in self.query) or ("i am also fine" in self.query) or ('all fine' in self.query) or ('all good' in self.query) or ('all is fine' in self.query) or ('all is good' in self.query)):
                speak("Its nice to hear from you")    
                self.query=self.takecommand().lower()
             
        elif(('how are you' in self.query) or ('what about you' in self.query) or ('are you fine' in self.query) or ("are you good" in self.query)):
                speak("I am good sir")
                speak("what about you")    
                self.query=self.takecommand().lower()
                
        while True:
            
            self.query = (self.takecommand().lower())
            # print(self.query)
            
    #  LOGIC BUILDING FOR TASKS
                
            # ---------------FOR NOTEPAD------------------- 
            if ("open notepad" in self.query) or ("open the notepad" in self.query) or ("open my notepad" in self.query) or  ("make a note" in self.query):
                speak("Sure Sir!")
                npath = "C:\\WINDOWS\\system32\\notepad.exe"        #notepad main path location
                
                # we use double slash(\\),bcz we can't use single slash(\) for finding the directory path
                # we are also writting \\notepad.exe after the file location of the notepad 
                
                os.startfile(npath)   #try to give such names to variables those doesn't match with builtin functions
            # like npath instead of path, to avoid any problem#by pressing Ctrl+click(mouse,etc), we can open that function,where it is defined
           
            #------for closing the notepad------
            elif ("close notepad" in self.query) or ("close the notepad" in self.query) or ("close the note" in self.query):
                speak("Okay Sir,Closing notepad!")    
                os.system("taskkill /f /im notepad.exe")   #for closing the notepad.exe
                # "taskkill","/F","/IM","notepad.exe"


            
            #----------------------------FOR CALCULATOR--------------------------- 
            elif(('open calculator'in self.query) or ('open the calculator'in self.query)) :
                speak("Okay Sir!")
                speak('Opening calculator')
                os.startfile('C:\\Windows\\System32\\calc.exe')
                
            # # #   #for closing the calculator
            elif (('close calculator'in self.query) or ('close the calculator'in self.query)) :
                speak("Sorry Sir, I am not able to close calculator")
                # os.system("taskkill /f /calculator.exe")   
                # ""C:\Windows\System32\calc.exe""   
            
            
            
            #----------------------- FOR OPENING THE VS CODE-----------------------------
            
            elif(('open the vs code'in self.query) or ('open vs code'in self.query) or ('open the visual studio'in self.query) or ('open visual studio'in self.query) or ('open visual studio code'in self.query) or ('open vscode'in self.query)) :
                    speak("Okay Sir!")
                    speak('Opening the Visual Studio')
                    os.startfile("C:\\Users\\yashs\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    
            elif(('close the vs code'in self.query) or ('close vs code'in self.query) or ('close the visual studio'in self.query) or ('close visual studio'in self.query) or ('close visualstudio'in self.query) or ('close vscode'in self.query)) :
                    speak("Okay Sir!")
                    speak('closing the visual studio')       
                    os.system("taskkill /f /im Code.exe")  
            
                
            # ----------------FOR COMMAND PROMPT----------------       
            elif("open cmd" in self.query) or ("open command prompt" in self.query):
                speak("Sure Sir!")
                speak("Launching command prompt")
                os.system("Start cmd")  #system will easily run the cmd
              
                # FOR CLOSING THE COMMAND PROMPT 
            elif ("close cmd" in self.query) or ("close the cmd" in self.query) or ("close the command prompt" in self.query):
                speak("Okay Sir,Closing cmd!")    
                os.system("taskkill /f /im cmd.exe")     
                
              # FOR VOLUME UP OF SYSTEM  
            elif(("volume up" in self.query) or ("increase volume" in self.query) or ("increase the volume" in self.query) or ("increase the sound" in self.query)):
                pyautogui.press("volumeup")
                speak('volume increased sir')
                
            #command for decreaseing the volume in the system
            #Eg: jarvis decrease volume
            elif(("volume down" in self.query) or ("decrease volume" in self.query) or ("decrease the volume" in self.query) or ("decrease the sound" in self.query)):
                pyautogui.press("volumedown")
                speak('volume decreased Sir')
            #Command to mute the system sound
            #Eg: jarvis mute the sound
            elif(("volume mute" in self.query) or ("mute the sound" in self.query) or ("mute the volume" in self.query)) :
                pyautogui.press("volumemute")
                speak('volume muted sir')     
                
           
                
            # ---------------FOR CAMERA----------------
            elif(("open camera" in self.query) or ("take a picture" in self.query) or ("click a picture" in self.query) or ("click a photo" in self.query) or ("take a photo" in self.query) or ("open the camera" in self.query) or ("launch the camera" in self.query) or ("capture a picture" in self.query) or ("capture a photo" in self.query)):
                speak("Sure Sir!")
                speak("I am taking the picture")
                
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame = videoCaptureObject.read()
                    speak("what will be the name of this image!")
                    names=self.takecommand().lower()
                    names=f"{names}"
                    # img.save(names)
                    cv2.imwrite(f"{names}.png",frame)
                    result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                speak("Sir, The picture has been saved in your main folder successfully")
            
            
             #------------- TO SHOW THE CAMERA PHOTO-----------------
            elif(("show the picture" in self.query) or ("open the image" in self.query)  or ("show me the clicked photo" in self.query) or ("show me the picture" in self.query) or ("open the picture" in self.query) or ("show the photo" in self.query) or ("show me the photo" in self.query) or ("open the photo" in self.query)):
                try:
                    
                    webbrowser.open(f"C:/Users/yashs/OneDrive/Desktop/JarvisGui/{names}.png")
                    speak("the image is opening")
                    
                    
                    #     imgs.save(names)
                    #     imgs = Image.open(open(f"C:/Users/yashs/OneDrive/Desktop/JarvisGui/{names}.png"))
                    #     speak("Picture is opening sir")
                    #     imgs.show(imgs)
                    #     time.sleep(2)
                    
                except IOError:   
                    speak("Sorry sir, I am unable to display the picture")    
            
            
            
            # elif(("open camera" in self.query) or ("open the camera" in self.query) or ("launch the camera" in self.query) or ("launch camera" in self.query)):
            #         speak("Sure Sir!")
            #         speak("Camera is opening!")
            #         name=self.takecommand().lower()
            #         speak("Please hold the screen for few seconds, I am taking photo")
            #         cap=cv2.VideoCapture(0) #(0) for internal camera,and we can write (1) for external camera or path of that camera
            #         while(True):
            #             ret,img= cap.read()
            #             cv2.imshow('webcam',img)
            #             cv2.imwrite("filename.jpg",img) #save image
            #             k=cv2.waitKey(50) #for wait
            #             name=f"{name}.png"
            #             img.save(name)
            #             if k==27:
            #                 break
            #         cap.release() #release the camera
            #         # cv2.imwrite("filename.jpg",img) #save image
            #         cv2.destroyAllWindows()
            
            
            
                # in open cv, camera doesn't stop by self, we 
                # have to stop that by pressing "escape(Esc)" on keyboard (when it opens in only read mode)
                
                
            #-------------------FOR SWITCH THE WINDOW--------------
            elif(("switch the window" in self.query) or ("switch the windows" in self.query) or ("switch between the windows" in self.query) or ("switch window" in self.query) or ("switch between windows" in self.query)):
                pyautogui.keyDown("alt") #keydown meaning press(firstly we key down the alt, then we press tab)
                pyautogui.press("tab") #press tab along with alt
                time.sleep(1) #take 1 second gap,after performing task
                pyautogui.keyUp("alt") #keyup is necessary, when we key down the alt key     
                
                            
        # ---------------FOR OPEN ONLINE THINGS----------------

            # ------FOR FINDING THE IP ADDRESS OF MY DEVICE
            elif("ip address" in self.query):
                ip=get("https://api.ipify.org").text
                speak(f"Your IP Address is {ip}")
                #in above line,f-string used,use f-string where we have to print a varibale in the string
                
                
            # FOR KNOWING THE DATE------------------    
            elif(("what is the date" in self.query) or ("tell me today date" in self.query) or ("tell me the date" in self.query) or ("what is the date today" in self.query)):
                dates = datetime.datetime.now().strftime("%b %d %Y")
                speak(f"Today is {dates}")
            
            # FOR KNOWING THE TIME------------------    
            elif(("what is the time" in self.query) or ("tell me the time" in self.query) or ("what is the time now" in self.query)):
                hour = int(datetime.datetime.now().hour)
                tts= time.strftime("%I:%M %p")
                speak(f"The time is {tts}")
                
                
            # FOR KNOWING THE DAY------------------
            elif(("what day is today" in self.query) or ("tell me today day" in self.query) or ("day of today" in self.query) or ("what is the day today" in self.query) or ("today is  what day" in self.query)):
                if(dt. date. today(). isoweekday() == 1):
                    speak("Sir Today is Monday")
                if(dt. date. today(). isoweekday() == 2):
                    speak("Sir Today is Tuesday")
                if(dt. date. today(). isoweekday() == 3):
                    speak("Sir Today is Wednesday")
                if(dt. date. today(). isoweekday() == 4):
                    speak("Sir Today is Thursday")
                if(dt. date. today(). isoweekday() == 5):
                    speak("Sir Today is Friday")
                if(dt. date. today(). isoweekday() == 6):
                    speak("Sir Today is Saturday")
                if(dt. date. today(). isoweekday() == 7):
                    speak("Sir Today is Sunday")
                    
                
            #------TO FIND THE LOCATION--------
            elif(("what is my location" in self.query) or("where i am" in self.query) or ("where we are" in self.query)):
                speak("Wait Sir, let me check!")
                try:
                    ipAdd= requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url="https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                    geo_requests= requests.get(url)
                    geo_data=geo_requests.json()
                    # city=geo_data["city"]
                    # state=geo_data["state"]
                    # print(state)
                    country=geo_data["country"]
                    speak(f"Sir, I am not very sure, but i think we are in  {country} country")
                except Exception as e:
                    speak("Sorry Sir, Due to network issue, I am not able to find where we are")
                    pass    
                
                
            #-------TO TAKE THE SCREENSHOT------
            elif(("take screenshot" in self.query) or ("take a screenshot" in self.query) or ("take the screenshot" in self.query)):
                speak("Sure Sir!")
                speak("what will be the name of this screenshot!")
                name=self.takecommand().lower()
                speak("Please hold the screen for few seconds, I am taking Screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                # img.save(f"{name}.png")
                name=f"{name}.png"
                img.save(name)
                speak("I am done Sir,The screenshot has been saved in the main folder!")
                
                
                
            #------------- TO SHOW THE SCREEN SHOT-----------------
            elif(("show the screenshot" in self.query) or ("show me the screenshot" in self.query) or ("open the screenshot" in self.query)):
                try:
                    img = Image.open(f"C:\\Users\\yashs\\OneDrive\\Desktop\\JarvisGui\\{name}")
                    speak("Screenshot is opening sir")
                    img.show(img)
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")
    
                
            #---------TO CHECK THE TEMPERATURE---------
            elif(("temperature" in self.query) or ("what is the temperature" in self.query) or ("what is the weather" in self.query) or ("how is the weather today" in self.query)):
                search="temperature in muzaffarnagar"
                url= f"https://www.google.com/search?q={search}"
                r= requests.get(url)
                data= BeautifulSoup(r.text,"html.parser")
                temp= data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}") 
                
            
            #-------------FOR OPEN YOUTUBE--------------        
            elif(("open youtube" in self.query) or ("play youtube" in self.query) or ("open the youtube" in self.query) or ("play the youtube" in self.query)):
                speak("Sure Sir!")
                webbrowser.open("www.youtube.com")
                speak("Youtube is going to be ready")
                
            #-------------FOR OPEN INSTAGRAM--------------        
            elif("instagram" in self.query):
                speak("Sure Sir!")
                webbrowser.open("www.instagram.com")
                speak("Instagram is opening...")

            #-------------FOR OPEN TWITTER--------------        
            elif("twitter" in self.query):
                speak("Sure Sir!")
                webbrowser.open("www.twitter.com")
                speak("Twitter is opening...")
                
            #-------------FOR OPEN LINKEDIN--------------        
            elif("linkedin" in self.query):
                speak("Sure Sir!")
                webbrowser.open("www.linkedin.com")
                speak("Linkedin is opening...")
                
            #-------------FOR OPEN WHATSAPP--------------        
            elif("whatsapp" in self.query):
                speak("Sure Sir!")
                webbrowser.open("www.whatsapp.com")
                speak("Whatsapp is opening...")
                
            #-------------FOR OPEN FACEBOOK--------------        
            elif("facebook" in self.query):
                speak("Sure Sir!")
                webbrowser.open("www.facebook.com")
                speak("Facebook is opening...")  
                
            #-------------FOR OPEN GOOGLE--------------  
            elif(("open chrome browser" in self.query) or ("open google chrome" in self.query) or ("open google" in self.query)):
                speak("Sure Sir!")
                webbrowser.open("www.google.com")
                speak("Google is opening...")  
            
            #-------- FOR CLOSING THE GOOGLE CHROME-------------------
             
            elif(("close google" in self.query) or ("close chrome browser" in self.query) or ("close google chrome" in self.query) or ("close the google chrome" in self.query)):
                speak("Ok sir, Google has been closed")
                os.system("taskkill /im chrome.exe /f")    
                
                
                
        #-----------FOR DIRECTLY SEARCH ON GOOGLE BY VOICE   
            elif(("on explorer" in self.query) or ("on internet" in self.query)or ("on browser" in self.query) or ("in browser" in self.query)or ("google about" in self.query) or ("on google" in self.query) or ("in google" in self.query) or ("search about" in self.query)):
                speak("Sure Sir!")
                # if("search" in self.query):
                # speak("Google is opening...")                   
                # speak("Sir, what you want to search on google...")
                # self.query=self.takecommand().lower()
                words=["search","search about","on browser","in browser", "from browser","jarvis","on google","in google","on internet","google about","open about","open"]
                for i in words:
                    self.query=(self.query).replace(i," ")
                res=" ".join((self.query).split())   
                speak(f"I am searching {res}")  
                webbrowser.open(f"{res}")
                # print(self.query)        
                    # speak("Okay Sir, I am searching on it")
                    
            elif(("close browser" in self.query) or ("close the browser" in self.query) or ("close the explorer" in self.query) or ("close the internet explorer" in self.query)):
                    speak("Ok sir, I am going to close Browser")
                    os.system("taskkill /im msedge.exe /f")  
                    
                    
                    
                # -----FOR LISTENING THE NEWS FROM JARVIS-----------
            elif(("read news" in self.query) or ("tell today news" in self.query) or ("read today news" in self.query) or ("read today highlights" in self.query) or ("breaking news" in self.query) or ("news" in self.query) or ("read today highlight" in self.query)):
                #url of key, that is of news api.org site,which will fetch the news(articles)
                my_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=c242c5be3d3d4c6b9e88345b2306e542" #for india
                open_my_page = requests.get(my_url).json()
                # print(open_my_page)
                my_articles= open_my_page["articles"]
                # print(my_articles)
                speak("Wait for a while,I am Searching the today's top news!")
                myresults=[]
                news_number=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
                for ar in my_articles:
                    myresults.append(ar["title"])
                    # speak("Here are the top today news!")
                    
                for i in range(len(news_number)): 
                    # print(f"today's {day[1]} news is",head[i])
                    # speak(f"{news_number[i]} news: {myresults[i]}")
                    speak(f"{news_number[i]} news: {myresults[i]}")
                    
                    
                    
        #------------------------FOR MUSIC-------------------
            elif(("open music" in self.query) or ("play music" in self.query)):
                speak("Sure Sir!")
                music_dir="C:\\Users\\yashs\\Music" #for file location music
                songs =os.listdir(music_dir) #to convert the songs in a list that is present in this music directory
                # os.startfile(os.path.join(music_dir,songs[0])) 
            #here, we dont need to write songs[0] ,in above line, bcz we are
            #using random module's rd function, to play random music.
                # rd=random.choice(songs)    #for playing random songs
                # os.startfile(os.path.join(music_dir,rd)) 
                # if i want to play only mp3 songs from a folder
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile(os.path.join(music_dir, song))
                        
            elif("close music" in self.query):    
                os.close(os.path.join(music_dir, song))#music function calling         
                    
    #---------------ACTIVATE HOW TO DO MODE-------------
            elif("activate how to do mode" in self.query):
                speak("Okay Sir")
                speak("How to do mode is activated")
                while True:
                    speak("Please tell me what you want to know, i am listening")
                    how=self.takecommand().lower()
                    try:
                        if ("exit" in how) or ("close" in how) or ("come out" in how):
                            speak("How to do mode has been deactivated")
                            break      
                        else:
                            max_results=1
                            how_to= search_wikihow(how, max_results)
                            assert len(how_to)==1
                            # how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("Sorry Sir, I am not able to find this")        
            #----------------TO TELL THE JOKES--------------------
            elif(("tell me a joke" in self.query) or ("tell me jokes" in self.query) or ("tell me some jokes" in self.query)):
                joke=pyjokes.get_joke()
                speak(joke)
                            
                    
        #  -------------WIKIPEDIA-------------- 
            elif(("in wikipedia" in self.query) or ("on wikipedia" in self.query) or ("wikipedia" in self.query)):
                # speak("Sir, What you want to Searching in Wikipedia...")
                # query=query.replace("wikipedia","")
                # query = takecommand().lower()
                results=wikipedia.summary(self.query,sentences=3)  
                # # in above line,sentences=2 means it will take 2 sentences from wikipedia
                speak("According to Wikipedia,")
                speak(results)        
        #----------- TO CHECK THE BATTERY PERCENTAGE-----
            elif(("what is the battery level" in self.query) or ("what is the battery percentage" in self.query) or ("how much power is left" in self.query) or ("battery" in self.query) or ("how much power we have" in self.query)):
                battery=psutil.sensors_battery()
                percentage= battery.percent
                speak(f"Sir, Our system have {percentage} percent battery")         
                
        #-----------------for shut down the system-----------------
            elif(("shutdown the system" in self.query) or ("shutdown the pc" in self.query) or ("close the system" in self.query) or ("close the pc" in self.query) or ("close my pc" in self.query)):
                # os.os.system("shutdown /s /t /5")
                os.system("shutdown /s /t 10")  #/s is for shut down the pc , 5 is for 5 seconds,it will say, that your system is going to shut down in 5 seconds
            
            
        #------------------for restart the system------------------------------ 
            elif(("restart the system" in self.query) or ("restart the pc" in self.query) or ("restart system" in self.query) or ("restart pc" in self.query) or ("restart my pc" in self.query)):
                os.system("shutdown /s /r /10") #pc will restart in 10 seconds
            
            
        #--------------------for sleep the pc----------------    
            elif(("sleep the system" in self.query) or ("sleep the pc" in self.query) or ("sleep system" in self.query) or ("sleep down " in self.query) or ("sleep pc" in self.query) or ("sleep my pc" in self.query)):
                speak("Okay Sir")
                # os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                
                # it will always write in last of the program
            # for exiting from the program after saying no thanks
            
        # --------------- TO SAY THE THANKS TO JARVIS-------- 
            elif(("thanks jarvis" in self.query) or ("thank you jarvis" in self.query)):
                speak("You're welcome Sir")
                # speak("I always find me happy to work for you")
                
            elif(("no thanks" in self.query) or ( "you can rest" in self.query)  or ("you can rest now" in self.query) or ("no thank you" in self.query) or ("you can sleep" in self.query) or ("you can go in sleep mode" in self.query)) :
                speak("ok sir, I am going to rest for a while,")
                speak("But,you can call me anytime.....I am available 24 7 for you")
                # speak("But,you can call me anytime.....I am available 24 7 for you")
                break # for breaking from this loop,  not exiting from the program
                
                
                
                
        # #---------------FOR ASKING OF ANY OTHER WORK----------------
        #     speak("Can I have more work Sir...")
        #     speak("I am in listening mode")
         
         
            
        #---------------FUNNY COMMANDS TO TALK WITH JARVIS--------------
            #Fun commands to interact with jarvis
            # elif(('hello jarvis' in self.query) or ('hey jarvis' in self.query) or ('hi jarvis' in self.query)):
            #     speak("Hello Sir")
            #     # speak("How are you!")
            #     self.query=self.takecommand().lower()
                
            # elif(('i am fine' in self.query) or ('i am good' in self.query)or ('i am also good' in self.query) or ("i am also fine" in self.query) or ('all fine' in self.query) or ('all good' in self.query) or ('all is fine' in self.query) or ('all is good' in self.query)):
            #     speak("Its nice to hear from you")    
            #     self.query=self.takecommand().lower()
             
            # elif(('how are you' in self.query) or ('what about you' in self.query) or ('are you fine' in self.query) or ("are you good" in self.query)):
            #     speak("I am good sir")
            #     speak("what about you")    
            #     self.query=self.takecommand().lower()
            
            elif (('what is your name' in self.query) or  ('tell me your name' in self.query) or  ('tell me about your name' in self.query)):
                speak("My name is jarvis")
                self.query=self.takecommand().lower()
            
            elif(('who is your master' in self.query) or  ('what is your master name' in self.query) or ('who is your creator' in self.query)):
                speak("My master's name are Yash Singhal and Varnika Singhal")
            
            
            elif (('what are they studying' in self.query) or  ('education of your master' in self.query) or ('what is your masters education' in self.query)or ('their course' in self.query)):
                speak("They are studying in Bachelor of Technology from Information Technology Branch") 
            
            
            elif (('what can you do' in self.query) or ('what is your expertise' in self.query)):
                speak("I can talk with you until you want to stop, I can say time,I can search for some thing in google and I can tell jokes, I can do many more things for you")
            
            elif('your age' in self.query):
                # speak("I am very young than you")
                speak("I am older than yesterday and younger than tommorow")
                speak("can you tell me your age?")
                
            elif ('are you there' in self.query):
                speak('Yes sir I am always here for you')\
                    
                 
            elif ('are you busy' in self.query or 'are you busy right now' in self.query or 'you are busy' in self.query):
                speak('No Sir, I am not busy')
                
            elif 'tell me something' in self.query:
                speak('boss, I don\'t have much to say, you can tell me someting i will give you the company')
                
            
            elif 'i love you' in self.query:
                speak('I love you too boss')
                
            
            elif(('can you hear me' in self.query) or ('are you listening' in self.query)):
                speak('Yes ofcourse sir, I can hear you')
                
            elif (('do you ever get tired' in self.query) or ('do you get tired' in self.query)):
                speak('It would be impossible to be tired of our conversation')
                
           
            elif (('are you feeling bored' in self.query) or ('are you boring' in self.query)):
                speak('It would be impossible to be tired of our conversation') 
                
            elif (('are you stupid' in self.query) or ('are you idiot' in self.query) or  ('you are stupid' in self.query)):
                speak('no, i am not. I think you have some misunderstanding...')    
               
            elif(('i am not fine' in self.query) or ('i am not good' in self.query) or ('all not fine' in self.query) or ('all not good' in self.query) or ('all is not fine' in self.query) or ('all not good' in self.query) or ('nothing is good' in self.query)  or ('all is not good' in self.query)):
                speak("what happen sir")
                speak("can i help you in something...")         
                
                
            elif(("goodbye" in self.query) or ("you can go offline" in self.query) or ("you can off" in self.query)  or ("you can deactivate" in self.query) or ("you can be off" in self.query)):
                    speak("Thanks for using me Sir, I am extremely happy to help you")
                    sys.exit()       
                
            
        #---------------FOR ASKING OF ANY OTHER WORK----------------
            speak("Sir, can i help you in something else... I am in listening mode")
            # speak("listening mode")    

                
startExecution=MainThread()                
            
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("button1.jpg")
        self.ui.label_1.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("giphy.gif")   #"jarvis-gif-unscreen (1).gif"
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("initial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("new3.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("iron man.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Start1.png")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Quit.png")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("jarvis new.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("g51.jpg")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("g51.jpg")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("jarvis gif.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis_Gui (1).gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
      
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())    