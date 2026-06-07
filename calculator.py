#ui start

import tkinter as Tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI CALCULATOR")

global opr

data_input = Entry(root,width=50)
data_input.grid(row=1,column=1,columnspan=3,rowspan=2)

#function
def button_click(number):
    data = str(data_input.get())
    data_input.delete(0,END)
    data_input.insert(0,data+str(number))
    
def clear_scr():
    data_input.delete(0,END)
    
def add():
    global f_num 
    global opr
    opr = "add"
    f_num = data_input.get()
    data_input.delete(0,END) 

def sub():
    global f_num
    global opr
    opr = "sub" 
    f_num = data_input.get()
    data_input.delete(0,END)

def mult():
    global f_num
    global opr
    opr = "mult" 
    f_num = data_input.get()
    data_input.delete(0,END)

def div():
    global f_num
    global opr
    opr = "div" 
    f_num = data_input.get()
    data_input.delete(0,END)
    
def equal():
    s_num = data_input.get()
    data_input.delete(0,END)
    if int(f_num) != None and int(s_num) != None:
        if opr == "add":
            data_input.insert(0,int(f_num)+int(s_num))
        elif opr == "sub":
            data_input.insert(0,int(f_num)-int(s_num))
        elif opr == "mult":
            data_input.insert(0,int(f_num)*int(s_num))
        elif opr == "div":
            data_input.insert(0,int(f_num)/int(s_num))
        else:
            data_input.insert(0,"something wrong")
    else:
        message = messagebox.showerror("Error","Something Wrong")
        Label(root,text=message).pack()


btn1 = Button(root,text="1",padx=40,pady=10,command=lambda:button_click(1)).grid(row=3,column=1)
btn2 = Button(root,text="2",padx=40,pady=10,command=lambda:button_click(2)).grid(row=3,column=2)
btn3 = Button(root,text="3",padx=40,pady=10,command=lambda:button_click(3)).grid(row=3,column=3)
btn4 = Button(root,text="4",padx=40,pady=10,command=lambda:button_click(4)).grid(row=4,column=1)
btn5 = Button(root,text="5",padx=40,pady=10,command=lambda:button_click(5)).grid(row=4,column=2)
btn6 = Button(root,text="6",padx=40,pady=10,command=lambda:button_click(6)).grid(row=4,column=3)
btn7 = Button(root,text="7",padx=40,pady=10,command=lambda:button_click(7)).grid(row=5,column=1)
btn8 = Button(root,text="8",padx=40,pady=10,command=lambda:button_click(8)).grid(row=5,column=2)
btn9 = Button(root,text="9",padx=40,pady=10,command=lambda:button_click(9)).grid(row=5,column=3)
btn0 = Button(root,text="0",padx=90,pady=10,command=lambda:button_click(0)).grid(row=6,column=1,columnspan=2)
equal = Button(root,text="=",padx=40,pady=10,command=equal).grid(row=6,column=3)
add = Button(root,text="+",padx=40,pady=10,command=add).grid(row=7,column=1)
sub = Button(root,text="-",padx=40,pady=10,command=sub).grid(row=7,column=2)
mult = Button(root,text="x",padx=40,pady=10,command=mult).grid(row=7,column=3)
div = Button(root,text="%",padx=88,pady=10,command=div).grid(row=8,column=1,columnspan=2)
clear = Button(root,text="Clear",padx=30,pady=10,command=clear_scr).grid(row=8,column=3)

#ui close



root.mainloop()