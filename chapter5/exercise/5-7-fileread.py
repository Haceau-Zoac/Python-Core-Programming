#!/usr/bin/env python

from tkinter import *
from os.path import isfile  
from time import sleep
from tkinter.filedialog import askopenfilename

class FileReader(object):

    def __init__(self):
        self.top = Tk()

        self.fmenu = Menu(self.top, tearoff=0)
        self.fmenu.add_command(label='打开', command=self.openfile)
        self.menu = Menu(self.top)
        self.menu.add_cascade(label='文件', menu=self.fmenu)
        self.menu.add_command(label='退出', command=self.top.quit)
        self.top.config(menu=self.menu)

        self.file = ''
        self.txtfm = Frame(self.top)
        self.txtsb = Scrollbar(self.top)
        self.txtsb.pack(side=RIGHT, fill=Y)
        self.txt = Text(self.txtfm, height=15,
            width=50, yscrollcommand=self.txtsb.set)
        self.txt.pack()
        self.txtfm.pack()
    
    def openfile(self, _=None):
        self.file = askopenfilename()
        self.readfile()

    def readfile(self, _=None):
        error = ''
        if not isfile(self.file):
            error = f'{self.file} 不是文件。'
        else:
            try:
                content = ''
                with open(self.file) as s:
                    content = s.read()
                self.txt.delete(1., END)
                self.txt.insert(1., content)
            except:
                error = '读取文件失败。'

        if error != '':
            self.txt.delete(1., END)
            self.txt.configure(fg='red')
            self.txt.insert(1., error)
            self.top.update()
            sleep(2)
            self.txt.delete(1., END)
            self.txt.configure(fg='white')
            self.top.update()

def main():
    FileReader()
    mainloop()

if __name__ == '__main__':
    main()