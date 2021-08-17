#!/usr/bin/env python

from tkinter import Tk, Spinbox
import tkinter
from tkinter.ttk import Style, Label, Button, Combobox

top = Tk()
Style().configure('TButton',
    foreground='white', background='red')

Label(top,
    text='动物（成对的；最少：一对；最多：一打）').pack()
Label(top, text='数量：').pack()

Spinbox(top, from_=2, to=12,
    increment=2, font='Helvetica -14 bold').pack()

Label(top, text='种类：').pack()

Combobox(top, values=('狗',
    '猫', '仓鼠', '蟒蛇')).pack()

Button(top, text='退出',
    command=top.quit, style='TButton').pack()


top.mainloop()