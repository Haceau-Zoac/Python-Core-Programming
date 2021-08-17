#!/usr/bin/env python

from tkinter import Button, END, Label, W
from Pmw import initialise, ComboBox, Counter

top = initialise()

lb = Label(top,
    text='动物（成对的；最少：一对；最多：一打）')
lb.pack()

ct = Counter(top, labelpos=W, label_text='数量：',
    datatype='integer', entryfield_value=2,
    increment=2, entryfield_validate={'validator':
    'integer', 'min': 2, 'max': 12})
ct.pack()

cb = ComboBox(top, labelpos=W, label_text='种类：')
for animal in ('狗', '猫', '仓鼠', '蟒蛇'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='退出',
    command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()