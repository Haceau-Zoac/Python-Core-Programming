#!/usr/bin/env python

import os
from sys import argv
from timeit import timeit
from threading import Thread

class ByteCounterThread(Thread):

    def __init__(self, byte, filename, filesize, nthread, cthread):
        Thread.__init__(self)
        self.byte = byte
        self.filename = filename
        self.nthread = nthread
        self.cthread = cthread
        self.bsize = filesize // self.nthread
        self.count = 0
    
    def run(self):
        self.bytecount()
    
    def get_result(self):
        return self.count

    def bytecount(self):
        with open(self.filename, 'rb') as f:
            start = self.bsize * self.cthread
            f.seek(start)
            data = f.read(self.bsize)
            for b in data:
                if b == self.byte:
                    self.count = self.count + 1

def bytecount_st():
    count = 0
    with open(filename, 'rb') as f:
        text = f.read()
        for b in text:
            if b == byte:
                count = count + 1
    print(count)
    return count

def bytecount():
    threads = []
    fs = os.stat(filename).st_size
    for i in range(0, nthread):
        threads.append(ByteCounterThread(byte, filename, fs, nthread, i))
    
    for i in range(nthread):
        threads[i].start()

    count = 0
    for i in range(nthread):
        threads[i].join()
        count = count + threads[i].get_result()
    print(count)

if len(argv) < 3:
    print(f'\tUsage: {argv[0]} <byte> <filename> [threadnum]')
else:
    byte = bytes(argv[1], 'utf-8')[0]
    filename = argv[2]
    nthread = int(argv[3]) if len(argv) > 3 else 3
    stime = timeit(stmt=bytecount_st, number=1)
    print(f'单线程：{stime} 秒')
    mtime = timeit(stmt=bytecount, number=1)
    print(f'多线程：{mtime} 秒')
    if stime > mtime:
        print(f'单线程是多线程速度的 {stime / mtime} 倍。')
    else:
        print(f'多线程是单线程速度的 {mtime / stime} 倍。')