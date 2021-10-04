# module imports
from tkinter import *
import os
from tkinter import messagebox
from mng_sys import login_page
from PIL import Image,ImageTk
from tkinter import Tk




# designing main window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x300")
    main_screen.title("Login Or Registration")
    main_screen.iconbitmap("C:/Users/hp/PycharmProjects/Std_mng_syst/Std_mng_syst/login.ico")



    Label(text="Login Or Registration",bd=4, bg="black",fg="white", width="310",font=("Times",20,"bold")).pack()
    Label(text="").pack(side=TOP,fill= X)

    frame1 = LabelFrame(main_screen,text="Choose to LOGIN OR REGISTER",bd=10,bg="light sky blue",relief=RIDGE)
    frame1.place(x=0,y=50,width=500,height=250)

    Button(frame1,text="Login", width="15",font=("Times", "12", "bold"),bd=5, command=login).grid(row=3, column=0)
    Button(frame1,text="Register", width="15",font=("Times", "12", "bold"),bd=5, command=register).grid(row=3, column=1)

    # images in left dataframe
    imglogin = Image.open("loginreg.PNG")
    imglogin = imglogin.resize((476, 180), Image.ANTIALIAS)
    photoimg2 = ImageTk.PhotoImage(imglogin)
    btn = Button(frame1, image=photoimg2, borderwidth=0)
    btn.place(x=0, y=38)




    main_screen.mainloop()




main_account_screen()