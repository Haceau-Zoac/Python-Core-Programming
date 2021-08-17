#!/usr/bin/env python

from tkinter import *
from tkinter.messagebox import askyesno
from os.path import isfile  
from time import sleep
from tkinter.filedialog import askopenfilename, asksaveasfile

class FileReader(object):

    def __init__(self):
        self.top = Tk()
        self.top.title('new.txt')
        self.file = 'new.txt'
        self.new = True

        self.fmenu = Menu(self.top, tearoff=0)
        self.fmenu.add_command(label='打开', command=self.openfile)
        self.fmenu.add_command(label='新建', command=self.create)
        self.fmenu.add_command(label='另存为', command=self.saveas)
        self.fmenu.add_command(label='保存', command=self.save)
        self.saved = True
        self.menu = Menu(self.top)
        self.menu.add_cascade(label='文件', menu=self.fmenu)
        self.menu.add_command(label='退出', command=self.quit)
        self.top.config(menu=self.menu)

        self.txtfm = Frame(self.top)
        self.txtsb = Scrollbar(self.top)
        self.txtsb.pack(side=RIGHT, fill=Y)
        self.txt = Text(self.txtfm, height=15,
            width=50, yscrollcommand=self.txtsb.set)
        self.txt.bind('<<Modified>>', self.txtmodified)
        self.txt.pack()
        self.txtfm.pack()

    def txtmodified(self, _=None):
        self.saved = False

    def openfile(self, _=None):
        if not self.saved:
            yes = askyesno('提示', '当前文件尚未保存，是否保存？')
            if yes:
                self.save()
        self.file = askopenfilename()
        if self.file:
            self.readfile()

    def quit(self, _=None):
        if not self.saved:
            yes = askyesno('提示', '当前文件尚未保存，是否保存？')
            if yes:
                self.save()
        self.top.quit()

    def create(self, _=None):
        self.top.title('new.txt')
        self.file = 'new.txt'
        self.new = True
        self.txt.delete(1., END)

    def save(self, _=None):
        if not isfile(self.file) or self.new:
            self.saveas()
        with open(self.file, 'w') as f:
            f.write(self.txt.get(1., END))
        self.saved = True

    def saveas(self, _=None):
        f = asksaveasfile()
        if f is not None:
            f.write(self.txt.get(1., END))
            self.file = f.name
            self.settitle()
            f.close()
            self.new = False
            self.saved = True

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
        else:
            self.new = False
            self.settitle()
            self.saved = True
    
    def settitle(self):
        index = self.file.rfind('/')
        print(index)
        self.top.title(self.file[index + 1 if index != -1 else 0:])

def main():
    FileReader()
    mainloop()

if __name__ == '__main__':
    main()