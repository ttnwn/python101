from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

GUI = Tk()
GUI.title('โปรแกรมออกกำลังกาย')
GUI.geometry('500x500')
GUI.config(bg='green')

#หัวข้อ
L1=Label(GUI, text='วันนี้ออกกำลังกายอะไรดี' , font = ('schoollife',40) , fg='blue')
L1.place(x=100 , y=50)

#button1 = เวลาในการออก
def Button1() :
    time = ['10' , '15', '20' , '25' , '30' , '40' , '50']
    A=random.choice(time)
    messagebox.showinfo('เวลาในการออกกำลังกาย' , A)
    
#ปุ่มเวลา
fb1 = Frame(GUI)
fb1.place(x=150 , y=150)
b1  = ttk.Button(fb1, text='ออกกำลังกายกี่นาทีดี' , command=Button1)
b1.pack(ipadx=40 , ipady = 40)

#trainer
def Button2() :
    trainer = ['bebe fit routine' , 'Chole Ting' , 'Pamela Reif' , 'Mad fit']
    b = random.choice(trainer)
    messagebox.showinfo('Trainer คนไหนดี' , b)

#ปุ่มสุ่ม trainer
fb2 = Frame(GUI)
fb2.place(x=150,y=220)
b2 = ttk.Button(fb2, text = 'Trainer เทรนใจ' , command=Button2)
b2.pack(ipadx=50,ipady=40)



GUI.mainloop()
