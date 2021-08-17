#!/usr/bin/env python

import tkinter
top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

bye = tkinter.Button(top, text='bye',
    command=lambda: hello.configure(text='Bye bye~'))
bye.pack(fill=tkinter.X, expand=1)

gui = tkinter.Button(top, text='gui',
    command=lambda: hello.configure(text='Hello GUI!'))
gui.pack(fill=tkinter.X, expand=1)

tk = tkinter.Button(top, text='tk',
    command=lambda: hello.configure(text='Hello Tkinter!'))
tk.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()