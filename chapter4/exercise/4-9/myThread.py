#!/usr/bin/env python

import threading

class MyThread(threading.Thread):
    def __init__(self, files):
        threading.Thread.__init__(self)
        self.files = files
    
    def getResult(self):
        return self.res
    
    def run(self):
        self.res = 0
        for file in self.files:
            with open(file) as f:
                self.res = self.res + len(f.readlines())