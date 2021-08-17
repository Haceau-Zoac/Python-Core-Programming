#!/usr/bin/env python

from tkinter import Label, Button, END
from tkinter.tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top,
    text='动物 (成对的；最少：一对；最多：一打)')
lb.pack()

ct = Control(top, label='数量：',
    integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label='种类：', editable=True)
for animal in ('狗', '猫', '仓鼠', '蟒蛇'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='退出',
    command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()