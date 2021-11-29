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
import winsound
showStr = lambda L: ' '.join(map(str, L))

showStr = lambda L: ' '.join(map(str, L))

word = ''
n = 0
ip = ''
index = 0
num = 0
start_pic = True
state = "idle"

class MyQueue(asyncio.Queue):

    def __init__(self):
        super().__init__()

    def shuffle(self):
        if self._queue is not self.empty():
         shuffle(self._queue)
        else: return None
        
deeee = MyQueue()

def ConvertString(string):
    tolist=[]
    tolist[:0]=string
    return tolist

def sc():
    global score
    print(score)
    score +=1

def validateLogin(username):
   print("username entered :", username.get())
   return
        
def showMainMenu():
    global mainmenu
    global pinPhoto1
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
    
   
    button_1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showSelectWorld()]).place(x=537, y=175)
    button_2 = Button(text="HOW TO",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showHowto()]).place(x=514, y=245)
    button_3 = Button(text="EXIT",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quitMainmenu).place(x=539, y=315)

    mainmenu.mainloop()

def play():
    winsound.PlaySound('s1.wav',winsound.SND_ASYNC)

def showSelectWorld():
    global selectworld
    selectworld = Tk()
    selectworld.title('PLAY')
    selectworld.geometry('1000x400')
    selectworld.resizable(width=False, height=False)

    pinPhotomode = Label(selectworld,bg = "#E9E8C8")
    pinPhotomode.place(x = 0, y = 0)
    image=Image.open("pic/mode.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotomode["image"] = picture
    pinPhotomode.image = picture

    user = Label(selectworld,text = username.get()+"    Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
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

    myLable5 = Button(text="PLAY",fg="#FFF6F0",font=('Tahoma', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[quitSelectWorld(),showGame()]).place(x=880, y=320)
    selectworld.mainloop()

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
    
# ===============================================================================================
def onKeyPress(event):
    print("Key press : ",event.char)
    global index
    global ip
    global word
    special_characters = "!@#$%^&*()-+?_=,<>/."
    #   checkisalpha            checkisspacebar     checkisnumber                checkisspecial_char
    if event.char.isalpha() or event.char == ' ' or event.char.isnumeric() or event.char in special_characters:
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(showgame, text=word[index], font='30', fg='black', bg = "#E9E8C8").grid(row=3, column=index)
            else:
                Label(showgame, text=word[index], font='30', fg='red', bg = "#E9E8C8").grid(row=3, column=index)
            index += 1

def pressBackSpace(event):
    global index
    global ip
    global word
    print("Key press : BackSpace")
    if index != 0:
        index -= 1
        ip = ip[:-1]
        Label(showgame, text=word[index], font='30', fg='grey', bg = "#E9E8C8").grid(row=3, column=index)

def pressEnter(event):
    global index
    global num
    global word
    global ip
    global start_pic
    start_pic = False
    Label(showgame, text='                   ',font = '30', bg = "#E9E8C8").place(x=0, y=35)
    if ip == word:
        Label(showgame,text='correct',fg = 'green',font = '30', bg = "#E9E8C8").place(x=0,y=35)
        #animation.playstage_good()
    else: 
        Label(showgame,text='not correct',fg = 'red',font = '30', bg = "#E9E8C8").place(x=0,y=35)
        #animation.playstage_bad()
    ip = ''
    index = 0
    #worldWords.showWorld()
    #inp.showWord()

def nothing(event):
    print('shift')
        
# ===============================================================================================
        
    
def showGame():
    global showgame
    showgame = Tk()
    showgame.title("GAME")
    showgame.geometry("1000x400")
    showgame.resizable(width=False, height=False)
    showgame.focus_force()
    countdowntime(20)
    userplay = Label(showgame,text = username.get()+"    Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    
    Check()
    
    #inp = GameInput(showgame)
    
    showgame.bind("<Return>", pressEnter)
    showgame.bind("<BackSpace>", pressBackSpace)
    showgame.bind('<KeyPress-Shift_L>',nothing) #กดShiftแล้วมันเข้า sp char ด้วย เลยต้องดัก shift ไว้ตรงนี้
    showgame.bind('<KeyPress-Shift_R>',nothing)
    showgame.bind("<KeyPress>",onKeyPress)
    
    showWorld()
    
    showgame.mainloop()
    
def Check():
    ch1 = Adjective.get()
    if ch1 == 1:
        print('World select: Adjective')
        Input('Adjective')
    ch2 = Animal.get()
    if ch2 == 1:
        print('World select: Animal')
        Input('Animal')
    ch3 = CarBrandName.get()
    if ch3 == 1:
        print('World select: CarID_Model')
        Input('CarID_Model')
    ch4 = CarID_Model.get()
    if ch4 == 1:
        print('World select: CarID_Model')
        Input('CarID_Model')
    ch5 = CarModel.get()
    if ch5 == 1:
        print('World select: CarModel')
        Input('CarModel')
    ch6 = Country.get()
    if ch6 == 1:
        print('World select: Country')
        Input('Country')
    ch7 = Fruits.get()
    if ch7 == 1:
        print('World select: Fruits')
        Input('Fruits')
    ch8 = Laptop.get()
    if ch8 == 1:
        print('World select: Laptop')
        Input('Laptop')

        
def Input(group):
    print("Load World : ",group)
    fileName = group
    asyncio.run(worldSelect(deeee, worldSearch(fileName)))
    
# ===============================================================================================

async def worldSelect(obj,fileName) :
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
            
        print(f'World : {fileName} --- Finish!')
    else:
        print("Not found")
        return -1
    
def worldSearch(inpFileName):
    csvFiles = []
    for file in glob.glob('DataWorld/AllWorld/*.csv'):
        directory = file.replace('DataWorld/AllWorld\\', '')
        directory =directory.replace('.csv', '')
        csvFiles.append(directory)
    print(csvFiles)
    for i in range(len(csvFiles)):
        if str(csvFiles[i]) == str(inpFileName):
            return csvFiles[i]
        else :
            if i == (len(csvFiles)-1):
                return None
            else: pass
            
async def getWorld(obj):
    obj.shuffle()
    while not obj.empty():
        tempGet = await obj.get()
        return tempGet
    
def showWorld():
    global word
    word = asyncio.run(getWorld(deeee))[0]
    print(f'Get word = {word}')
    
    for count in range(0,20):
        Label(showgame, text=' ', font='30',bg = "#E9E8C8").grid(row = 3, column = count)
    for count in range(0,len(word)):
        Label(showgame,text=word[count],font = '30',fg = 'grey',bg = "#E9E8C8").grid(row = 3,column = count)
    Label(showgame, text='                                                                           ', font='30', bg = "#E9E8C8").place(x=0, y=90)
    
def countdowntime(count_time):
    labeltime = Label(showgame,text=count_time,font = '20',background="#E9E8C8").place(x=930,y=0)

    if(count_time==9):  #แก้บัค:ตัวเลขซ้อน 
        Label(text="9 ",font = '20',bg="#E9E8C8").place(x=933,y=0)
    
    if(count_time > 0):
        showgame.after(1000,countdowntime,count_time-1)

    else:
        confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
        if(confirm=="ok"):
            showgame.destroy()
            
# ===============================================================================================
    
# ออกจากหน้าแต่ละหน้า
def quitMainmenu():
        mainmenu.destroy()
def quitHowto():
        howto.destroy()
def quitSelectWorld():
        selectworld.destroy()
def quitShowgame():
        showgame.destroy()
        
def highscore_read():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def highscore_write():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

# จุดเริ่มต้นโปรแกรม
if __name__ == '__main__':
    score = 0
    play()
    showMainMenu()
