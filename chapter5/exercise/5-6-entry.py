#!/usr/bin/env python

import tkinter
top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

radio = tkinter.IntVar(0)

entry = tkinter.Entry(top)
entry.insert(0, 'Hello World!')
entry.pack()

update = tkinter.Button(top, text='update',
    command=lambda: hello.configure(text=entry.get()))
update.pack()


tkinter.mainloop()