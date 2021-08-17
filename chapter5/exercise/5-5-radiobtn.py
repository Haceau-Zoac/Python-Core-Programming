#!/usr/bin/env python

import tkinter
top = tkinter.Tk()

texts = ['Bye bye~', 'Hello GUI!', 'Hello Tkinter!']

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

radio = tkinter.IntVar(0)

update = tkinter.Button(top, text='update',
    command=lambda: hello.configure(text=texts[radio.get()]))
update.pack(fill=tkinter.X, expand=1)

bye = tkinter.Radiobutton(top, text='bye', variable=radio,
    value=0)
bye.pack(fill=tkinter.X, expand=1)

gui = tkinter.Radiobutton(top, text='gui', variable=radio,
    value=1)
gui.pack(fill=tkinter.X, expand=1)

tk = tkinter.Radiobutton(top, text='tk', variable=radio,
    value=2)
tk.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()