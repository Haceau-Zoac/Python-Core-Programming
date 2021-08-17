#!/usr/bin/env python

from os import listdir
from time import time
from myThread import MyThread

def main():
    dir = input('dir > ')
    nthreads = int(input('threads > '))
    lines = 0
    threads = []
    connect = "\\" if dir[-1] == "\\" else "\\\\"
    files = listdir(dir)
    nfiles = len(files)
    for i in range(nfiles):
        files[i] = dir + connect + files[i]
    if nthreads > nfiles:
        print(f'线程太多了！！')
        return
    step = nfiles // nthreads

    start = time()
    i = 0
    while i < nfiles:
        thread = MyThread(files[i : i+step if i+step < nfiles else -1])
        thread.start()
        threads.append(thread)
        i = i + step
    
    for thread in threads:
        thread.join()
        lines = lines + thread.getResult()
    end = time() - start

    print(f'{int(end)} 秒。')

if __name__ == '__main__':
    main()