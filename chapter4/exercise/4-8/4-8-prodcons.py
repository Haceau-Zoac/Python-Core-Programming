#!/usr/bin/env python

# 参考 https://github.com/schedutron/CPAP/blob/master/Chap4/thread_pools.py

from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread
from sys import argv

def writeQ(queue):
    print('producing object for Q...',
        queue.put('xxx'))
    print('size now:', queue.qsize())

def readQ(queue):
    if queue.get(1):
        print('comsumed object from Q... size now',
            queue.qsize())
    else:
        print('Q currently empty...')

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = int(argv[1])
    q = Queue(32)
    nconsumers = int(argv[2])

    if nloops < nconsumers:
        print(f'Too many threads for {nloops} loops. Use less threads.')
        return

    threads = [MyThread(writer, (q, nloops), writer.__name__)]
    for i in range(nconsumers):
        t = MyThread(reader, (q, nloops // nconsumers), f'consumer {i}')
        threads.append(t)
        
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

    print('all DONE')

if __name__ == '__main__':
    main()