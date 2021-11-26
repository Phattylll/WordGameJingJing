from tkinter import*
from PIL import ImageTk,Image
from functools import partial
#from operator import itemgetter
import pickle
from time import time

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

def quit1():
        root.destroy()

def quit2():
        window2.destroy()
def quit3():
        window1.destroy()

def showMainMenu():
    global root
    root = Tk()
    bg1 = PhotoImage(file = "pic/st2.png")

    root.title("Game")
    canvas1 = Canvas( root, width = 1000,height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg1,  anchor = "nw")
    usernameLabel = Label(root, text="User Name",fg="#FAAF30",font=('Tahoma', 15, 'bold'),bg="#FFF6F0").place(x=427, y=100)
    global username
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username).place(x=547, y=110)
    buttonN()
    global validateLogin
    validateLogin = partial(validateLogin, username)
    cWin()
    root.mainloop()

def showWindowMenu1():
    global window1 
    window1 = Tk()  
    window1.geometry('1000x400')  
    window1.title('PLAY')
    bg3 = PhotoImage(file = "pic/mode.png")

    canvas3 = Canvas( window1, width = 1000,height = 400)
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, image = bg3,  anchor = "nw")
    #window1.after(1000,sc())
    #window1.after(1000,sc())
    user = Label(window1,text = username.get()+"    Score :     "+str(score),font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    '''
    myMenu1 = Menu()
    menuItem1 = Menu(tearoff=0)
    menuItem1.add_command(label="Hard" , command=lambda:[quit2(),showWindowMenu4()])
    menuItem1.add_command(label="Normal")
    menuItem1.add_command(label="Easy")
    myMenu1.add_cascade(label="Mode",menu=menuItem1,)
    window1.config(menu=myMenu1)
    '''
    myLable5 = Button(text="BACK",fg="#FFF6F0",font=('Tahoma', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[quit3(),showMainMenu()]).place(x=880, y=320)
    window1.mainloop()

def hide(x):
    x.pack_forget()

def showWindowMenu2():
    global window2
    window2 =Tk()
    window2.title("HOW TO")
    window2.geometry("1000x400")
    bg2 = PhotoImage(file = "pic/howto.png")
    canvas2 = Canvas( window2, width = 1000,height = 400)
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg2,  anchor = "nw")
    global myLable4
    myLable4 = Button(text="BACK",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quit2(),showMainMenu()]).place(x=30, y=320)

    window2.mainloop()
def showWindowMenu3():
    window3 =Tk()
    window3.title("SCORE")
    window3.geometry("1000x400")
    window3.mainloop()
def showWindowMenu4():
    window4 =Tk()
    window4.title("HARD")
    window4.geometry("1000x400")
    user = Label(window4,text = username.get()+"    Score :",font=('Tahoma', 20, 'bold')).place(x=0,y=0)
    window4.mainloop()
    myMenu2 = Menu()
    menuItem2 = Menu(tearoff=0)
    menuItem2.add_command(label="Food")
    menuItem2.add_command(label="Animal")
    menuItem2.add_command(label="Fruit")
    menuItem2.add_command(label="Internal Organs")
    menuItem2.add_command(label="Family")
    menuItem2.add_command(label="Occupations")
    menuItem2.add_command(label="Places")
    myMenu2.add_cascade(label="Category",menu=menuItem2)
    window4.config(menu=myMenu2)
    window4.mainloop()
def cWin():
    global check
    if check == True:
        print("window on")
        root.geometry("1000x400")
        check = False
    return check
def buttonN():
    myLable1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[validateLogin(),quit1(),showWindowMenu1()]).place(x=537, y=175)
    myLable2 = Button(text="HOW TO",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quit1(),showWindowMenu2()]).place(x=514, y=245)
    myLable3 = Button(text="EXIT",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quit1).place(x=539, y=315)
    return

#https://stackoverflow.com/questions/23949906/highscores-using-python-saving-10-highscores-and-ordering-them 

#-----------------------------------------------Main

check = True
score = 0
highscore_read()
showMainMenu()