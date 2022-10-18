from numpy import take
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser as wb
from telegram import Location
import wikipedia
import subprocess
import os
import time
from time import sleep
import pyjokes
import random
from requests import get
import pywhatkit as kit
import sys
import pyautogui, time 
import requests
import webbrowser
import cv2
import instaloader
import turtle
from turtle import *
from tkinter import *
from tkinter import messagebox
import random
from sketchpy import library as lib

time.sleep(2)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
voicespeed = 190
engine.setProperty('rate', voicespeed)
chrome_path = "C:/Program Files (x86)Google/Chrome/Application/chrome.exe %s "


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print(e)
        return"---"
    return query



def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)



def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)



def wishme():
    speak("welcome back sir")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    elif hour>=18 and hour<=24:
        speak("good evening")
    else:
        speak("good night")
    speak('''
    i am jarvis,
    please tell me how may i help you''')





def open_chrome():
    url = "https://www.google.co.in/"
   
    wb.get(chrome_path).open(url)













if __name__=="__main__":

# def TaskExecution():
    # speak()
    wishme()
    

# def taskexe():


    while True:
        query = takecommand().lower()
        print(query)
        
        if "good morning" in query:
            speak("good morning sir..")

        elif "time" in query:
            time()

        elif "date" in query:
            date()

        elif "open chrome" in query:
            open_chrome()

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)

        elif "search" in query:
            speak = ("what should i search??")
            search = takecommand().lower()
            wb.get(chrome_path).open_new_tab(search + ".com")

        elif "open youtube" in query:
            wb.open("www.youtube.com")

        elif "open google" in query:
            wb.open("www.google.com")

        elif "open notepad" in query:
            speak("opening notepad")
            Location = "C:\\Windows\\system32\\notepad.exe"
            notepad = subprocess.Popen(Location)

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()

        elif "joke" in query:
            joke = pyjokes.get_jokes()
            speak(joke)

        elif "logout" in query:
            speak("loging out in 5 second")
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown the system" in query or "the system" in query:
            speak("shutting down in 5 second")
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak("restarting in 5 second")
            sleep(5)
            os.system("shutdown /r /t 1")
            


        elif "jarvis are you here" in query or "are you here" in query:
            speak("I am here sir")

        elif "open command prompt" in query:
            speak("open command prompt")
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0) 
            while True:
                rat, img = cap.read()
                cv2.imshow('web cam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "F:\\New folder\\New folder (2)"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "thank you" in query:
            speak("my pleasure sir")

        elif "kya kar rahe ho" in query:
            speak("i am feel bored sir")

        # elif "hay" in query:
        #     speak("hello sir")

        elif "open facebook" in query:
            wb.open("www.facebook.com")
        elif "close " in query:
            pyautogui.hotkey('alt', 'f4')

        elif "open instagram" in query:
            wb.open("www.instagram.com")
        

        # elif "send message" in query:
        #     kit.sendwhatmsg("+916002835530", "toi chuze ka baccha",8,58)

        elif "you can sleep now" in query or "sleep now" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            # time.sleep(1)
            pyautogui.keyUp("alt")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir,   let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir, i am not sure, but i think we are in {city} city of {country}")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are")
                pass

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir, please enter the user name correctly.")
            name = input("Enter the user name here:-")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir, here is the profile of the user {name}")
            # time.sleep(5)
            speak("sir, would you download profile picture of this accouny??")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir,  profile picture is save on our main folder. now i am ready for next command..")
            else:
                pass


        # elif "take screeshot" in query or "take a screenshot" in query:
        #     speak("sir,  please tell me the name of these screenshot file.")
        #     name = takecommand().lower()
        #     speak("please sir,  hold the screenfor few second .. i am taking a screenshot")
        #     # time.sleep(5)
        #     img = pyautogui.screenshot()
        #     img.save(f"{name}.png")
        #     speak("sir, i am done, the screenshot is save o our main folder, now i am ready for next command")



        elif "hide all files" in query or "hide this folder" in query or "make it visible for everyone" in query:
            speak("sir, please tell me you want to hide this folder or make it visible for everyone?")            
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("all the files in this folder are now visible for everyone.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

            else:
                pass

        elif "open this pc" in query:
            speak("opening this pc")
            pyautogui.doubleClick(35,138)

        elif "close this pc" in query:
            speak ("ok sir")
            pyautogui.click(1349,4)
            



        elif "open paint" in query:
            speak("opening paint")
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)


        elif "hidden menu" in query:
            pyautogui.hotkey('winleft', 'x')


        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            pyautogui.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("D:\\ss.png")
            speak('done')

        elif "new desktop" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "hello jarvis" in query or "hello" in query:
            speak('hello sir')
        elif "what are you doing" in query:
            speak("waiting for your command sir")

        elif "close command prompt" in query:
            speak("closing command prompt")
            pyautogui.hotkey('alt', 'f4')

        elif "close paint" in query:
            speak("closing paint")
            pyautogui.hotkey('alt', 'f4')

        elif "play song on youtube" in query:
            kit.playonyt("www.youtube.com","see you again")

        elif "can you help me" in query:
            speak("yes, ofcource sir..")
        
            
        elif "draw what you want" in query or "what you want" in query:
            speak ("ok")
            # time.sleep(5)
            
            pyautogui.click()
            distance = 200

            while distance >0:
                pyautogui.dragRel(distance, 0,  duration=0.2)
                distance = distance-5
                pyautogui.dragRel(0, distance, duration=0.2)

                pyautogui.dragRel(-distance, 0, duration=0.2)
                distance = distance-5
                pyautogui.dragRel(0, -distance, duration=0.2)
                pass 

        elif"open local disk d" in query:
            speak("ok")
            pyautogui.doubleClick(853, 302)
        
        elif "check message" in query or "message" in query:
            speak("ok")
            pyautogui.click(38, 366)

        elif "scroll" in query: 
            for i in range(100):
                pyautogui.scroll(-300)
                
        elif "do you love me" in query:
            if 1:
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)
                speak("i am just a program sir")
                

        elif "so you don't love me" in query:
            speak("if i become a girl then i accept your proposal sir")

        elif "ok" in query:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)
            speak("thankyou sir")

        elif "draw vibrate circle" in query or "vibrate circle" in query:
            speak("ok sir")
            t = turtle.Turtle()
            s = turtle.Screen()
            s.bgcolor("black")
            t.pencolor("white")
            a = 0
            b = 0
            t.speed(0)
            t.penup()
            t.goto(0,200)
            t.pendown()
            while True:
                t.forward(a)
                t.right(b)
                a+=3
                b+=1
                if b == 210:
                    break
                t.hideturtle()

            turtle.done()

        elif "draw a flower" in query or " flower" in query:
            speak("ok")
            for i in range(300):
                tu = turtle.Turtle()
                # tu.screen.bgcolor("black")pip install pyaudio  
                # tu.color("orange")

                circle(190-i,90)
                left(90)
                circle(190-i,90)
                left(18)
                speed(0)
            mainloop()
            pass 

        elif "draw a beautiful tree" in query or "beautiful tree" in query:
            speak("sure sir")
            tu = turtle.Turtle()
            tu.screen.bgcolor("black")
            tu.pensize(2)
            tu.color("green")
            tu.left(90)
            tu.backward(100)
            tu.speed(200)
            tu.shape('turtle')

            def tree(i):
                if i<10:
                    return
                else:
                    tu.forward(i)
                    tu.color("orange")
                    tu.circle(2)
                    tu.color("brown")
                    tu.left(30)
                    tree(3*i/4)
                    tu.right(60)
                    tree(3*i/4)
                    tu.left(30)
                    tu.backward(i)

            tree(100)
            turtle.done()
            speak("done sir")

        elif "mera chutiya best friend ke liye kush bolo" in query or "best friend" in query:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[3].id)
            speak("आपका बेस्ट फ्रेंड एक नम्बर का हरामी हे sir")
        
        elif "tumhare khayal se wo ab kya kar raha hoga" in query or "khayal" in query:
            # voices = engine.getProperty('voices')
            # engine.setProperty('voice', voices[3].id)
            speak(" क्या करेगा वो  कहीं पे बेकार परा हुआ है सायड,   उसका तो कुश काम धंदा है नाही")

        elif"kya sach me" in query:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)
            speak("yes sir")
        elif "are you sure" in query or "sure" in query:
            speak("100 percent sure sir")
            


###################     TIC TAC TOE ####################
        


        elif "jarvis" in query or "service" in query:
            speak("yes sir")

        elif"can i play tic tac toy" in query or "tic tac to" in query:
            speak("ofcource sir ,  now you can play")
            class TIC_TAC_TOE_AI:
                def __init__(self, root):
                    # Basic Initialization
                    self.window = root
                    self.make_canvas = Canvas(self.window, background="#141414", relief=RAISED, bd=3)
                    self.make_canvas.pack(fill=BOTH, expand=1)

                    self.machine_cover = []
                    self.human_cover = []
                    self.prob = []
                    self.sign_store = {}
                    
                    self.chance_counter = 0
                    self.technique = -1
                    
                    self.surrounding_store = {1: (2,3,4,7), 2:(1,3), 3:(1,2,6,9), 4:(1,7), 5: (2,4,6,8), 6: (3,9), 7:(1,4,8,9), 8:(7,9), 9:(7,8,6,3)}            

                    self.decorating()

                def decorating(self):# Basic Set-up
                    Label(self.make_canvas, text="Tic-Tac-Toe AI", bg="#141414", fg="#00FF00", font=("Lato", 25, "bold")).place(x=110, y=10)
                    self.btn_1 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(1), state=DISABLED)
                    self.btn_1.place(x=20,y=100)
                    self.btn_2 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(2), state=DISABLED)
                    self.btn_2.place(x=190,y=100)
                    self.btn_3 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(3), state=DISABLED)
                    self.btn_3.place(x=360,y=100)

                    self.btn_4 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(4), state=DISABLED)
                    self.btn_4.place(x=20,y=200)
                    self.btn_5 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(5), state=DISABLED)
                    self.btn_5.place(x=190,y=200)
                    self.btn_6 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(6), state=DISABLED)
                    self.btn_6.place(x=360,y=200)

                    self.btn_7 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(7), state=DISABLED)
                    self.btn_7.place(x=20,y=300)
                    self.btn_8 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(8), state=DISABLED)
                    self.btn_8.place(x=190,y=300)
                    self.btn_9 = Button(self.make_canvas, text="", font=("Arial", 15, "bold", "italic"), width=5, bg="#262626", activebackground="#262626", bd=3, command=lambda: self.__human_play(9), state=DISABLED)
                    self.btn_9.place(x=360,y=300)

                    self.activate_btn = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]

                    self.machine_first_control = Button(self.make_canvas, text="Machine vs Human", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", fg="#9d9dff", relief=RAISED, bd=3, command=lambda: self.control_give("machine_first"))
                    self.machine_first_control.place(x=15, y=380)

                    self.human_first_control = Button(self.make_canvas, text="Human vs Machine", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", fg="#9d9dff", relief=RAISED, bd=3, command=self.control_give)
                    self.human_first_control.place(x=240, y=380)

                    self.reset_btn = Button(self.make_canvas, text="Reset", font=("Arial", 15, "bold", "italic"), bg="#262626", activebackground="#262626", disabledforeground="grey", fg="#9d9dff", relief=RAISED, bd=3, command=self.reset, state=DISABLED)
                    self.reset_btn.place(x=190, y=440)

                def reset(self):# Reset the game
                    self.machine_cover.clear()
                    self.human_cover.clear()
                    self.sign_store.clear()
                    self.prob.clear()
                    self.technique = -1
                    self.chance_counter = 0
                    for every in self.activate_btn:
                        every.config(text="")
                    self.machine_first_control['state'] = NORMAL
                    self.human_first_control['state'] = NORMAL
                    self.reset_btn['state'] = DISABLED
                
                def game_over_management(self):# After game over some works
                    for every in self.activate_btn:
                        every.config(state=DISABLED)
                    self.reset_btn['state'] = NORMAL
                
                def control_give(self, indicator="human_first"):# Control give based on human first or computer first play
                    self.machine_first_control.config(state=DISABLED, disabledforeground="grey")
                    self.human_first_control.config(state=DISABLED, disabledforeground="grey")
                    self.reset_btn.config(state=DISABLED, disabledforeground="grey")
                    for every in self.activate_btn:
                        every.config(state=NORMAL)
                    if indicator == "machine_first":
                        self.__machine_play()
                    
                def __sign_insert(self, btn_indicator, sign_is="X"):# Button sign Insert
                    if sign_is == "X":
                        self.activate_btn[btn_indicator - 1].config(text=sign_is, state=DISABLED, disabledforeground="#00FF00")
                    else:
                        self.activate_btn[btn_indicator - 1].config(text=sign_is, state=DISABLED, disabledforeground="red")
                    self.sign_store[btn_indicator] = sign_is
                
                def __machine_play(self):# Machine Control
                    self.chance_counter+=1
                    # For even in self.chance_counter, human first chance..... for odd, computer first chance
                    if self.chance_counter == 1:
                        self.__sign_insert(9)
                        self.machine_cover.append(9)

                    elif self.chance_counter == 2:
                        human_last = self.human_cover[len(self.human_cover)-1]
                        if human_last != 5:
                            self.technique = 1
                            self.__sign_insert(5)
                            self.machine_cover.append(5)
                        else:
                            self.technique = 2
                            self.__sign_insert(9)
                            self.machine_cover.append(9)
                                
                    elif self.chance_counter == 3:
                        human_input = self.human_cover[len(self.human_cover)-1]
                        if human_input%2 == 0:
                            self.technique = 1
                            self.activate_btn[5 - 1].config(text="X")
                            self.sign_store[5] = "X"
                            self.prob.append(1)

                        elif human_input != 5:
                            self.technique = 2
                            take_prediction = [7,3]
                            try:
                                take_prediction.remove(human_input)
                            except:    
                                pass
                            take_prediction = random.choice(take_prediction)
                            self.__sign_insert(take_prediction)
                            self.prob.append(1)
                            self.machine_cover.append(take_prediction)
                        else:
                            self.technique = 3
                            self.__sign_insert(1)

                    elif self.chance_counter == 4:
                        human_first = self.human_cover[0]
                        human_last = self.human_cover[1]
                        opposite = {1:9, 2:8, 3:7, 4:6, 6:4, 7:3, 8:2, 9:1}

                        if self.technique == 1:
                            take_surr = list(self.surrounding_store[human_first])
                            if human_last in take_surr:
                                take_surr.remove(human_last)
                                diff = human_last - human_first

                                if diff == 6 or diff == -6:
                                    if diff == 6:
                                        place_it = human_first + 3
                                    elif diff == -6:
                                        place_it = human_first - 3
                                elif diff == 2 or diff == -2:
                                    if diff == 2:
                                        place_it = human_first + 1
                                    else:
                                        place_it = human_first - 1
                                elif diff == 1 or diff == -1:
                                    if diff == 1:
                                        if human_first-1 == 1 or human_first-1 == 7:
                                            place_it = human_first-1
                                        else:
                                            place_it = human_last+1
                                    else:
                                        if human_last-1 == 1 or human_last-1 == 7:
                                            place_it = human_last-1
                                        else:
                                            place_it = human_first+1
                                elif diff == 3 or diff == -3:
                                    if diff == 3:
                                        if human_first-3 == 1 or human_first-3 == 3:
                                            place_it = human_first-3
                                        else:
                                            place_it = human_last+3
                                    else:
                                        if human_last-3 == 1 or human_last-3 == 3:
                                            place_it = human_last-3
                                        else:
                                            place_it = human_first+3

                                self.__sign_insert(place_it)
                                self.machine_cover.append(place_it)
                                self.prob.append(opposite[place_it])
                                self.surrounding_store[human_first] = tuple(take_surr)
                            else:
                                if 2 not in self.sign_store.keys():
                                    self.__sign_insert(2)
                                    self.machine_cover.append(2)
                                    if opposite[2] not in self.sign_store.keys():
                                        self.prob.append(opposite[2])
                                else:
                                    temp = [4,6,8]
                                    take_total = self.human_cover+self.machine_cover
                                    for x in take_total:
                                        if x in temp:
                                            temp.remove(x)
                                    take_choice = random.choice(temp)
                                    self.__sign_insert(take_choice)
                                    self.machine_cover.append(take_choice)
                                    self.prob.append(opposite[take_choice])

                        elif self.technique == 2:
                            human_last = self.human_cover[len(self.human_cover)-1]
                            if human_last == 1:
                                take_place = 3
                                self.prob.append(4)
                                self.prob.append(6)
                            else:
                                take_place = opposite[human_last]
                                diff = 9 - take_place
                                if diff == 2:
                                    self.prob.append(9-1)
                                elif diff == 6:
                                    self.prob.append(9-3)
                                elif diff == 3:
                                    self.prob.append(9-6)
                                else:
                                    self.prob.append(9-2)
                            self.__sign_insert(take_place)
                            self.machine_cover.append(take_place)

                    elif self.chance_counter == 5:
                        human_input = self.human_cover[len(self.human_cover)-1]
                        if self.technique == 1:
                            if self.prob[0] != human_input:
                                self.__sign_insert(self.prob[0])
                                self.machine_line_match()
                            else:
                                if self.technique == 1:
                                    try:
                                        try:
                                            if self.sign_store[self.prob[0]+1] == "O":
                                                pass
                                        except:
                                            if self.sign_store[self.prob[0]+1+6] == "O":        
                                                pass
                                        value_take = self.prob[0]+2
                                        self.prob.clear()
                                        self.prob.append(6)
                                        self.prob.append(7)
                                    except:
                                        value_take = self.prob[0]+6
                                        self.prob.clear()
                                        self.prob.append(8)
                                        self.prob.append(3)
                                    
                                    self.__sign_insert(value_take)  
                                    self.machine_cover.append(value_take)
                            
                        elif self.technique == 2:
                                if self.machine_cover[0] - self.machine_cover[1] == 6:
                                    try:
                                        if self.sign_store[self.machine_cover[1]+3] == "O":
                                            self.prob.clear()
                                            if 7 in self.sign_store.keys():
                                                value_predict = 1
                                                self.prob.append(2)
                                            else:
                                                value_predict = 7
                                                self.prob.append(8)    
                                            self.prob.append(5)    
                                            self.__sign_insert(value_predict)  
                                            self.machine_cover.append(value_predict)
                                    except:
                                        self.__sign_insert(self.machine_cover[1]+3)  
                                        self.machine_line_match()
                                else:
                                    try:
                                        if self.sign_store[self.machine_cover[1]+1] == "O":
                                            self.prob.clear()
                                            if 3 in self.sign_store.keys():
                                                value_predict = 1
                                                self.prob.append(4) 
                                            else:
                                                value_predict = 3
                                                self.prob.append(6) 
                                            self.prob.append(5)     
                                            self.__sign_insert(value_predict)    
                                            self.machine_cover.append(value_predict)
                                    except:
                                        self.__sign_insert(self.machine_cover[1]+1)  
                                        self.machine_cover.append(self.machine_cover[1]+1)
                                        self.machine_line_match()
                        else:
                            if self.prob:
                                self.prob.clear()
                            draw_occurance =  {2: 8, 8: 2, 4: 6, 6: 4}
                            if human_input in draw_occurance.keys():
                                self.technique = 3.1
                                self.__sign_insert(draw_occurance[human_input])  
                                self.machine_cover.append(draw_occurance[human_input])
                                next_prob = {8: 7, 4: 7, 2: 3, 6: 3}
                                self.prob.append(next_prob[draw_occurance[human_input]])
                            else:
                                self.technique = 3.2
                                if human_input == 3:
                                    self.__sign_insert(7)  
                                    self.machine_cover.append(7)
                                    self.prob.append(8)
                                    self.prob.append(4)
                                else:
                                    self.__sign_insert(3)  
                                    self.machine_cover.append(3)
                                    self.prob.append(2)
                                    self.prob.append(6)
                                
                    elif self.chance_counter == 6:
                        if self.human_line_match():
                            opposite = {1:9, 2:8, 3:7, 4:6, 6:4, 7:3, 8:2, 9:1}
                            human_last = self.human_cover[len(self.human_cover)-1]
                            if self.technique == 1:
                                if self.prob and human_last != self.prob[0]:
                                    self.__sign_insert(self.prob[0])
                                    self.machine_cover.append(self.prob[0])
                                    self.machine_line_match()
                                
                                elif len(self.prob) == 0:
                                    if human_last+3 == 7 or human_last+3 == 9:
                                        take_place = human_last+3
                                    elif human_last-3 == 1 or human_last-3 == 3:
                                        take_place = human_last-3
                                    elif human_last-3 == 4 or human_last-3 == 6:
                                        take_place = human_last-3
                                    elif human_last+3 == 4 or human_last+3 == 6:
                                        take_place = human_last+3
                                    
                                    self.__sign_insert(take_place)
                                    self.machine_cover.append(take_place)
                                    self.prob.append(opposite[take_place])

                                else:
                                    if self.prob:
                                        self.prob.clear()
                                    if human_last%2 == 0:
                                        if human_last == 8:
                                            if (human_last+1==3 or human_last+1==9) and human_last + 1 not in self.sign_store.keys():
                                                place_here = human_last + 1
                                            elif (human_last-1==1 or human_last-1==7) and human_last - 1 not in self.sign_store.keys(): 
                                                place_here = human_last - 1
                                            elif (human_last-3==1 or human_last-3==3) and human_last - 3 not in self.sign_store.keys(): 
                                                place_here = human_last - 3
                                            else:
                                                place_here = human_last + 3
                                            
                                            self.__sign_insert(place_here)
                                            self.machine_cover.append(place_here)
                                            temp_oppo = {7: 3, 3: 7, 1: 9, 9: 1}
                                            self.prob.append(temp_oppo[place_here])

                                        else:
                                            take_center_surr = list(self.surrounding_store[5])
                                            temp_store = self.human_cover+self.machine_cover
                                            for element in temp_store:
                                                try:
                                                    take_center_surr.remove(element)
                                                except:
                                                    pass
                                            
                                            if take_center_surr:
                                                if (human_last+3==7 or human_last+3==9) or human_last+3 in self.sign_store.keys():
                                                    take_place = human_last-3
                                                else:
                                                    take_place = random.choice(take_center_surr)
                                                    take_center_surr.remove(take_place)
                                                self.__sign_insert(take_place)
                                                self.machine_cover.append(take_place)
                                                self.surrounding_store[5] = tuple(take_center_surr)
                                                self.prob.append(opposite[take_place])
                                            else:
                                                for every in opposite.keys():
                                                    if every%2 != 0 and opposite[every] not in self.sign_store.keys():
                                                        self.__sign_insert(every)
                                                        self.machine_cover.append(every)
                                                        self.prob.append(opposite[every])
                                                        if (every+6 == 7 or every+6 == 9) and (every+6 not in self.sign_store.keys()):
                                                            self.prob.append(every+6)
                                                        elif (every-6 == 1 or every-6 == 3) and (every-6 not in self.sign_store.keys()):
                                                            self.prob.append(every-6)
                                                        elif (every-2 == 1 or every-2 == 7) and (every-2 not in self.sign_store.keys()):
                                                            self.prob.append(every-2)
                                                        else:
                                                            self.prob.append(every+2)
                                                        break
                                    else:
                                        take_surr = self.surrounding_store[human_last]
                                        for element in take_surr:
                                            if element in self.sign_store.keys():
                                                pass
                                            else:
                                                self.__sign_insert(element)
                                                self.machine_cover.append(element)
                                                if opposite[element] not in self.sign_store.keys():
                                                    self.prob.append(opposite[element])
                                                break
                            
                            else:
                                if len(self.prob) == 2:
                                    if human_last in self.prob:
                                        
                                        if self.prob[1] != human_last:
                                            self.__sign_insert(self.prob[1])
                                            self.machine_cover.append(self.prob[1])
                                            self.machine_line_match()

                                        else:
                                            self.__sign_insert(self.prob[0])
                                            self.machine_cover.append(self.prob[0])
                                            self.prob.clear()
                                            self.prob.append(2)
                                    else:
                                        self.__sign_insert(self.prob[1])
                                        self.machine_cover.append(self.prob[1])
                                        self.machine_line_match()
                                else:
                                    if human_last != self.prob[0]:
                                        self.__sign_insert(self.prob[0])
                                        self.machine_cover.append(self.prob[0])
                                        self.machine_line_match()
                                    else:
                                        self.__sign_insert(opposite[self.prob[0]])
                                        self.machine_cover.append(opposite[self.prob[0]])
                    
                    elif self.chance_counter == 7:
                        human_input = self.human_cover[len(self.human_cover)-1]
                        if self.technique == 1:
                            if self.prob[0] == human_input:
                                self.__sign_insert(self.prob[1])  
                            else:
                                self.__sign_insert(self.prob[0])  
                            self.machine_line_match()

                        elif self.technique == 2:
                            if human_input in self.prob:
                                self.prob.remove(human_input) 
                            self.__sign_insert(self.prob[0])  
                            self.machine_line_match()
                        else:
                            if self.technique == 3.2:
                                if human_input in self.prob:
                                    self.prob.remove(human_input)
                                self.__sign_insert(self.prob[0])  
                                self.machine_line_match()
                            else:
                                if human_input in self.prob:
                                    self.prob.clear()
                                    machine_next_chance = {7: 3, 3: 7}
                                    self.__sign_insert(machine_next_chance[human_input])
                                    next_human_prob = {3: (2,6), 7: (4,8)}
                                    self.prob.append(next_human_prob[machine_next_chance[human_input]][0])
                                    self.prob.append(next_human_prob[machine_next_chance[human_input]][1])
                                else:
                                    self.__sign_insert(self.prob[0])
                                    self.machine_line_match()

                    elif self.chance_counter == 8:
                        if self.human_line_match():
                            human_last = self.human_cover[len(self.human_cover)-1]
                            opposite = {1:9, 2:8, 3:7, 4:6, 6:4, 7:3, 8:2, 9:1}
                            
                            if self.technique == 1:
                                if self.prob and human_last not in self.prob:
                                    if self.prob[0] not in self.sign_store.keys():
                                        self.__sign_insert(self.prob[0])
                                        self.machine_cover.append(self.prob[0])
                                    else:
                                        temp=[1,2,3,4,5,6,7,8,9]
                                        temp_store = self.machine_cover + self.human_cover
                                        for x in temp_store:
                                            if x in temp:
                                                temp.remove(x)
                                        take_choice = random.choice(temp)
                                        self.__sign_insert(take_choice)
                                        self.machine_cover.append(take_choice)
                                    self.machine_line_match()

                                elif len(self.prob) == 0:
                                    self.__sign_insert(human_last+2)
                                    self.machine_cover.append(human_last+2)

                                else:
                                    if len(self.prob) == 2:
                                        if human_last in self.prob:
                                            self.prob.remove(human_last)
                                        self.__sign_insert(self.prob[0])
                                        self.machine_cover.append(self.prob[0])
                                        self.machine_line_match()

                                    else:
                                        take_surr = self.surrounding_store[human_last]
                                        for element in take_surr:
                                            if element in self.sign_store.keys():
                                                pass
                                            else:
                                                self.__sign_insert(element)
                                                self.machine_cover.append(element)
                                                break

                            else:
                                if opposite[human_last] not in self.sign_store.keys():
                                    self.__sign_insert(opposite[human_last])
                                    self.machine_cover.append(opposite[human_last])
                                else:
                                    temp_store = [1,2,3,4,5,6,7,8,9]
                                    temp_total = self.machine_cover+self.human_cover
                                    for element in temp_store:
                                        if element in temp_total:
                                            temp_store.remove(element)
                                    take_choice = random.choice(temp_store)
                                    self.__sign_insert(take_choice)
                                    self.machine_cover.append(take_choice)
                    
                    elif self.chance_counter == 9:
                        human_input = self.human_cover[len(self.human_cover)-1]
                        if self.prob[0] in self.sign_store.keys() and self.prob[1] in self.sign_store.keys():
                            self.prob.clear()
                            opposite_detection = {2: 8, 8: 2, 6: 4, 4: 6}
                            self.__sign_insert(opposite_detection[human_input])
                            self.machine_line_match()
                        else:
                            
                            if self.prob[0] in self.sign_store.keys():
                                self.__sign_insert(self.prob[1])
                            else:
                                self.__sign_insert(self.prob[0])
                            self.machine_line_match()


                def __human_play(self, chance):# Human Control
                    self.chance_counter+=1
                    self.__sign_insert(chance, "O")
                    self.human_cover.append(chance)
                    if self.chance_counter == 9:
                        self.human_line_match()
                    else:    
                        self.__machine_play()
                
                def machine_line_match(self):
                    found = 0
                    if self.activate_btn[1-1]['text'] == self.activate_btn[2-1]['text'] == self.activate_btn[3-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[4-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[6-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[7-1]['text'] == self.activate_btn[8-1]['text'] == self.activate_btn[9-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[1-1]['text'] == self.activate_btn[4-1]['text'] == self.activate_btn[7-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[2-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[8-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[3-1]['text'] == self.activate_btn[6-1]['text'] == self.activate_btn[9-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[1-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[9-1]['text'] == "X":
                        found=1
                    elif self.activate_btn[3-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[7-1]['text'] == "X":
                        found=1
                    if found == 1:
                        messagebox.showinfo("Game Over", "Computer is winner")
                        self.game_over_management()
                    elif self.chance_counter == 9:
                        messagebox.showinfo("Game Over", "Game draw")
                        self.game_over_management()
                
                def human_line_match(self):
                    found = 0
                    if self.activate_btn[1-1]['text'] == self.activate_btn[2-1]['text'] == self.activate_btn[3-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[4-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[6-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[7-1]['text'] == self.activate_btn[8-1]['text'] == self.activate_btn[9-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[1-1]['text'] == self.activate_btn[4-1]['text'] == self.activate_btn[7-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[2-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[8-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[3-1]['text'] == self.activate_btn[6-1]['text'] == self.activate_btn[9-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[1-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[9-1]['text'] == "O":
                        found=1
                    elif self.activate_btn[3-1]['text'] == self.activate_btn[5-1]['text'] == self.activate_btn[7-1]['text'] == "O":
                        found=1
                    if found == 1:
                        messagebox.showinfo("Game Over", "You are winner")
                        self.game_over_management()
                        return 0
                    elif self.chance_counter == 9:
                        messagebox.showinfo("Game Over", "Game draw")
                        self.game_over_management()
                        return 0
                    else:
                        return 1


            if __name__ == "__main__":
                window = Tk()
                window.title("AI Tic-Tac-Toe")
                window.config(bg="#141414")
                window.geometry("450x500")
                window.maxsize(450,500)
                window.minsize(450,500)
                TIC_TAC_TOE_AI(window)
                window.mainloop()
                                          



                         
##################    DORAEMON    #####################


        elif "draw doraemon" in query or "doraemon" in query:
            speak("ok sir")
            def ankur(x, y):
                penup()
                goto(x, y)
                pendown()


            def aankha():
                fillcolor("#ffffff")
                begin_fill()

                tracer(False)
                a = 2.5
                for i in range(120):
                    if 0 <= i < 30 or 60 <= i < 90:
                        a -= 0.05
                        lt(3)
                        fd(a)
                    else:
                        a += 0.05
                        lt(3)
                        fd(a)
                tracer(True)
                end_fill()


            def daari():
                ankur(-32, 135)
                seth(165)
                fd(60)

                ankur(-32, 125)
                seth(180)
                fd(60)

                ankur(-32, 115)
                seth(193)
                fd(60)

                ankur(37, 135)
                seth(15)
                fd(60)

                ankur(37, 125)
                seth(0)
                fd(60)

                ankur(37, 115)
                seth(-13)
                fd(60)


            def mukh():
                ankur(5, 148)
                seth(270)
                fd(100)
                seth(0)
                circle(120, 50)
                seth(230)
                circle(-120, 100)


            def muflar():
                fillcolor('#e70010')
                begin_fill()
                seth(0)
                fd(200)
                circle(-5, 90)
                fd(10)
                circle(-5, 90)
                fd(207)
                circle(-5, 90)
                fd(10)
                circle(-5, 90)
                end_fill()


            def nak():
                ankur(-10, 158)
                seth(315)
                fillcolor('#e70010')
                begin_fill()
                circle(20)
                end_fill()


            def black_aankha():
                seth(0)
                ankur(-20, 195)
                fillcolor('#000000')
                begin_fill()
                circle(13)
                end_fill()

                pensize(6)
                ankur(20, 205)
                seth(75)
                circle(-10, 150)
                pensize(3)

                ankur(-17, 200)
                seth(0)
                fillcolor('#ffffff')
                begin_fill()
                circle(5)
                end_fill()
                ankur(0, 0)


            def face():
                fd(183)
                lt(45)
                fillcolor('#ffffff')
                begin_fill()
                circle(120, 100)
                seth(180)
                # print(pos())
                fd(121)
                pendown()
                seth(215)
                circle(120, 100)
                end_fill()
                ankur(63.56, 218.24)
                seth(90)
                aankha()
                seth(180)
                penup()
                fd(60)
                pendown()
                seth(90)
                aankha()
                penup()
                seth(180)
                fd(64)


            def taauko():
                penup()
                circle(150, 40)
                pendown()
                fillcolor('#00a0de')
                begin_fill()
                circle(150, 280)
                end_fill()


            def Doraemon():
                taauko()

                muflar()

                face()

                nak()

                mukh()

                daari()

                ankur(0, 0)

                seth(0)
                penup()
                circle(150, 50)
                pendown()
                seth(30)
                fd(40)
                seth(70)
                circle(-30, 270)

                fillcolor('#00a0de')
                begin_fill()

                seth(230)
                fd(80)
                seth(90)
                circle(1000, 1)
                seth(-89)
                circle(-1000, 10)

                # print(pos())

                seth(180)
                fd(70)
                seth(90)
                circle(30, 180)
                seth(180)
                fd(70)

                # print(pos())
                seth(100)
                circle(-1000, 9)

                seth(-86)
                circle(1000, 2)
                seth(230)
                fd(40)

                # print(pos())

                circle(-30, 230)
                seth(45)
                fd(81)
                seth(0)
                fd(203)
                circle(5, 90)
                fd(10)
                circle(5, 90)
                fd(7)
                seth(40)
                circle(150, 10)
                seth(30)
                fd(40)
                end_fill()

                seth(70)
                fillcolor('#ffffff')
                begin_fill()
                circle(-30)
                end_fill()

                ankur(103.74, -182.59)
                seth(0)
                fillcolor('#ffffff')
                begin_fill()
                fd(15)
                circle(-15, 180)
                fd(90)
                circle(-15, 180)
                fd(10)
                end_fill()

                ankur(-96.26, -182.59)
                seth(180)
                fillcolor('#ffffff')
                begin_fill()
                fd(15)
                circle(15, 180)
                fd(90)
                circle(15, 180)
                fd(10)
                end_fill()

                ankur(-133.97, -91.81)
                seth(50)
                fillcolor('#ffffff')
                begin_fill()
                circle(30)
                end_fill()
                # Doraemon with Python Turtle

                ankur(-103.42, 15.09)
                seth(0)
                fd(38)
                seth(230)
                begin_fill()
                circle(90, 260)
                end_fill()

                ankur(5, -40)
                seth(0)
                fd(70)
                seth(-90)
                circle(-70, 180)
                seth(0)
                fd(70)

                ankur(-103.42, 15.09)
                fd(90)
                seth(70)
                fillcolor('#ffd200')
                # print(pos())
                begin_fill()
                circle(-20)
                end_fill()
                seth(170)
                fillcolor('#ffd200')
                begin_fill()
                circle(-2, 180)
                seth(10)
                circle(-100, 22)
                circle(-2, 180)
                seth(180 - 10)
                circle(100, 22)
                end_fill()
                goto(-13.42, 15.09)
                seth(250)
                circle(20, 110)
                seth(90)
                fd(15)
                dot(10)
                ankur(0, -150)

                black_aankha()


            if __name__ == '__main__':
                screensize(800, 600, "#f0f0f0")
                pensize(3)
                speed(9)
                Doraemon()
                ankur(100, -300)
                write('by AJ Chetia', font=("Bradley Hand ITC", 30, "bold"))
                mainloop()
                        

                   
                          
                                
        elif "draw tony stark" in query or "tony stark" in query:
            speak("ok sir")
            obj = lib.rdj()
            obj.draw()
            speak("done sir")







        


#     while True:
#         permission = takecommand()
#         if "wake up" in permission:
#             TaskExecution()
#         elif "good bye" in permission:
#             sys.exit()
