from tkinter import *
from os import access, close, path, read
from tkinter.colorchooser import *
import tkinter.messagebox
from typing import Counter, Sized
from tkinter.filedialog import *
import winsound
import time
from PIL import ImageTk, Image
from functools import partial
#from operator import itemgetter
import pickle
from time import time
import csv
from secrets import randbelow
import asyncio
from random import shuffle
import glob
from playsound import playsound
#import winsound
showStr = lambda L: ' '.join(map(str, L))

'''
text = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh']
word = text[0]
ip = ""
index = 0
num = 0
start_pic = True
game = Tk()
state = "idle"
class GameInput:
    
    def __init__(self, key):
        self.active_animation = True
        self.c = Label(game, bg = "#E9E8C8")
        for i in range(0, 3):
            Label(game, text = "",background="#E9E8C8").grid(row = i, column = 0)
        self.showWord()
        animation.run()
    def showWord(self):
        global word
        for n in range(0, 20):
            Label(game, text = " ", font = "30",background="#E9E8C8").grid(row = 3, column = n)
        for n in range(0, len(word)):
            Label(game, text = word[n], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = n)
        Label(game, text = '                                      ', font = "30",background="#E9E8C8").place(x = 0, y = 90)
        Label(game, text = f'Next word : {text[num + 1]}', font = "30",background="#E9E8C8").place(x = 0, y = 90)
    def onKeyPress(self, event):
        global index, ip
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(game, text = word[index], font = "30", fg = "black",background="#E9E8C8").grid(row = 3, column = index)
            else:
                Label(game, text = word[index], font = "30", fg = "red",background="#E9E8C8").grid(row = 3, column = index)
            index += 1
        print(event.char)
    def pressBackSpace(self, event):
        global index, ip
        print("backspace")
        if index != 0:
            index -= 1
            ip = ip[:-1]
            Label(game, text = word[index], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = index)
        
    def pressEnter(self, event):
        global index, num, word, ip, start_pic, state
        Label(game, text = '                   ', font = "30",background="#E9E8C8").place(x = 0, y = 35)
        start_pic = False
        if ip == word:
            state = "good"
            print("correct")
            Label(game, text = "correct", fg = "green", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()
        else:
            state = "bad"
            print("incorrect")
            Label(game, text = "incorrect", fg = "red", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()
        ip = ""
        index = 0
        num += 1
        word = text[num]
        self.showWord()
class App(GameInput):
    def __init__(self, key):
        self.currentFrame_good = 0
        self.currentFrame_bad = 179
        self.currentFrame_default = 255
        self.break_good = 0
        self.pinPhoto = Label(game, bg = "#E9E8C8")
   # def playsong(self):
    #    winsound.PlaySound("//Users//Pun Punyawat//OneDrive//Desktop//2D//datastr//game//song_noodle.wav",winsound.SND_ASYNC)
        
    def run(self):
        global state, start_pic
        if state == "idle":
            #print("idle work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_default += 1
            image=Image.open("pic_png/animation_png/default/eat-"+str(self.currentFrame_default)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_default == 271:
                self.currentFrame_default = 255
                #state = "idle"
                print(state)
            if state == "idle":
                game.after(10, self.run)
        elif state == "good":
            #print("good work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_good += 1
            image=Image.open("pic_png/animation_png/good//eat-"+str(self.currentFrame_good)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_good == 40:
                self.currentFrame_good = 0
                state = "idle"
                #start_pic = True
                print(state)
                return 
            if state == "good":
                game.after(10, self.run)
        elif state == "bad":
            #print("bad work")
            self.pinPhoto.place(x = 10, y = 200)
            time.sleep(0.02)
            self.currentFrame_bad += 1
            image=Image.open("pic_png//animation_png//bad//eat-"+str(self.currentFrame_bad)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_bad == 220:
                self.currentFrame_bad = 179
                state = "idle"
                #start_pic = True
                print(state)
                return
            if state == "bad":
                game.after(10, self.run)
    def countdowntime(self,count_time):
        labeltime = Label(game,text=count_time,background="#E9E8C8");
        labeltime.place(x=250,y=150);
        if(count_time > 0):
            game.after(1000,self.countdowntime,count_time-1);
        else:
            confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
            if(confirm=="ok"):
                game.destroy()   # ani.countdowntime(15) #นับเวลา
'''
class MyQueue(asyncio.Queue):

    def __init__(self):
        super().__init__()

    def shuffle(self):
        if self._queue is not self.empty():
         shuffle(self._queue)
        else: return None

def ConvertString(string):
    tolist=[]
    tolist[:0]=string
    return tolist

def worldSearch(inpFileName):
    csvFiles = []
    for file in glob.glob('DataWorld/AllWorld/*.csv'):
        directory = file.replace('DataWorld/AllWorld\\', '')
        directory =directory.replace('.csv', '')
        #directory = directory.strip('.csv')
        csvFiles.append(directory)
    print(csvFiles)
    for i in range(len(csvFiles)):
        if str(csvFiles[i]) == str(inpFileName):
            return csvFiles[i]
        else :
            if i == (len(csvFiles)-1):
                return None
            else: pass


async def worldSelect(obj,fileName) :
    print(f'Name : {fileName}')
    if fileName is not None :
        with open('DataWorld/AllWorld/'+fileName+'.csv', newline='') as f:
            reader = csv.reader(f)
            temp = list(reader)
            while len(temp) != 0:
                pos = randbelow(len(temp))
                # output type
                await obj.put(temp[pos])
                #await obj.put(ConvertString(showStr(temp[pos])))
                del temp[pos]
    else:
        print("Not found")
        return -1


async def getWorld(obj):
    obj.shuffle()
    #print(obj.__str__())
    while not obj.empty():
        tempGet = await  obj.get()
        Label(text=tempGet[0]).pack()
        return tempGet


#https://stackoverflow.com/questions/23949906/highscores-using-python-saving-10-highscores-and-ordering-them    hiscore

def highscore_read():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def highscore_write():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def sc():
    global score
    print(score)
    score +=1

def validateLogin(username):
   print("username entered :", username.get())
   return

def quitMainmenu():
        mainmenu.destroy()
def quitHowto():
        howto.destroy()
def quitPlaygame():
        playgame.destroy()
        
d = MyQueue()
def Input(group):
    fileName = group
    asyncio.run(worldSelect(d, worldSearch(fileName)))
def Check():

    #while d.empty() is False:
    #
    ch1 = Adjective.get()
    if ch1 == 1:
        #Label(text="select Adjective").pack()
        print('run file Adjective')
        Input('Adjective')

    ch2 = Animal.get()
    if ch2 == 1:
       # Label(text="select Animal").pack()
        print('run file Animal')
        Input('Animal')
    ch3 = CarBrandName.get()
    if ch3 == 1:
       # Label(text="select CarID_Model").pack()
        print('run file CarID_Model')
        Input('CarID_Model')
    ch5 = CarModel.get()
    if ch5 == 1:
       # Label(text="select CarModel").pack()
        print('run file CarModel')
        Input('CarModel')
    ch6 = Country.get()
    if ch6 == 1:
       # Label(text="select Country").pack()
        print('run file Country')
        Input('Country')
    ch7 = Fruits.get()
    if ch7 == 1:
      #  Label(text="select Fruits").pack()
        print('run file Fruits')
        Input('Fruits')
    ch8 = Laptop.get()
    if ch8 == 1:
      #  Label(text="select Laptop").pack()
        print('run file Laptop')
        Input('Laptop')

def showMainMenu():
    global mainmenu
    global pinPhoto1
    #global x
    #x=1
    #print(x)
    mainmenu = Tk()

    mainmenu.title("Game")
    mainmenu.geometry("1000x400")
    mainmenu.resizable(width=False, height=False)
    pinPhoto1 = Label(mainmenu,bg = "#E9E8C8")
    pinPhoto1.place(x = 0, y = 0)
    image=Image.open("pic/st2.png")
    picture = ImageTk.PhotoImage(image)
    pinPhoto1["image"] = picture
    pinPhoto1.image = picture
    usernameLabel = Label(mainmenu, text="User Name",fg="#FAAF30",font=('Tahoma', 15, 'bold'),bg="#FFF6F0").place(x=427, y=100)
    
    global username
    username = StringVar()
    usernameEntry = Entry(mainmenu, textvariable=username).place(x=547, y=110)
    global validateLogin
    validateLogin = partial(validateLogin, username)
    
   # button_1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showPlaygame()]).place(x=537, y=175)
    button_1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showPlaygame()]).place(x=537, y=175)
    button_2 = Button(text="HOW TO",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showHowto()]).place(x=514, y=245)
    button_3 = Button(text="EXIT",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quitMainmenu).place(x=539, y=315)
    button_song = Button(text="song",fg="red",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = play).place(x=905, y=340)
    mainmenu.mainloop()
    
   # lambda:[mainmenu.mainloop()]
def play():
    playsound('s1.mp3')

def showPlaygame():
    global playgame
    playgame = Tk()
    playgame.title('PLAY')
    playgame.geometry('1000x400')
    playgame.resizable(width=False, height=False)

    pinPhotomode = Label(playgame,bg = "#E9E8C8")
    pinPhotomode.place(x = 0, y = 0)
    image=Image.open("pic/mode.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotomode["image"] = picture
    pinPhotomode.image = picture

    user = Label(playgame,text = username.get()+"    Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    global Adjective
    Adjective = IntVar()
    Checkbutton(text = "Adjective",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Adjective).place(x=100,y=120)
    global Animal
    Animal = IntVar()
    Checkbutton(text = "Animal",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Animal).place(x=320,y=120)
    global CarBrandName
    CarBrandName = IntVar()
    Checkbutton(text = "CarBrandName",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = CarBrandName).place(x=100,y=190)
    global CarID_Model
    CarID_Model = IntVar()
    Checkbutton(text = "CarID_Model",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = CarID_Model).place(x=320,y=190)
    global CarModel
    CarModel = IntVar()
    Checkbutton(text = "CarModel",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = CarModel).place(x=100,y=260)
    global Country
    Country = IntVar()
    Checkbutton(text = "Country",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Country).place(x=320,y=260)
    global Fruits
    Fruits = IntVar()
    Checkbutton(text = "Fruits",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Fruits).place(x=100,y=330)
    global Laptop
    Laptop = IntVar()
    Checkbutton(text = "Laptop",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Laptop).place(x=320,y=330)

    myLable5 = Button(text="PLAY",fg="#FFF6F0",font=('Tahoma', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[Check(),showgame()]).place(x=880, y=320)
    playgame.mainloop()

def hide(x):
    x.pack_forget()

def showHowto():
    global howto
    howto = Tk()
    
    howto.title("HOW TO")
    howto.geometry("1000x400")
    howto.resizable(width=False, height=False)
    pinPhotohowto = Label(howto,bg = "#E9E8C8")
    pinPhotohowto.place(x = 0, y = 0)
    image=Image.open("pic/howto.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotohowto["image"] = picture
    pinPhotohowto.image = picture
 
    global myLable4
    myLable4 = Button(text="BACK",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitHowto(),showMainMenu()]).place(x=30, y=320)
    
    howto.mainloop()
    
def showWindowMenu3():
    window3 =Tk()
    window3.title("SCORE")
    window3.geometry("1000x400")
    window3.resizable(width=False, height=False)
    window3.mainloop()
def showgame():
    window4 =Tk()
    window4.title("GAME")
    window4.geometry("1000x400")
    window4.resizable(width=False, height=False)
    user = Label(playgame,text = username.get()+"    Score :     "+str(score),fg="red",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    window4.mainloop()
  


def main():
    animation = App(game)
    inp = GameInput(game)
   

    game.bind("<Return>", inp.pressEnter)
    game.bind("<BackSpace>", inp.pressBackSpace)
    game.bind("<KeyPress>", inp.onKeyPress)

    game.title("Noodle game")
    game.geometry("1000x800")

    game.config(bg = "#E9E8C8")

# animation.playsong()
    animation.countdowntime(15)
    game.mainloop()


#https://stackoverflow.com/questions/23949906/highscores-using-python-saving-10-highscores-and-ordering-them 

#-----------------------------------------------Main
score = 0
showMainMenu()
play()