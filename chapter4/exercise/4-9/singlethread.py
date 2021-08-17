#!/usr/bin/env python

from os import listdir
from time import time

dir = input('dir > ')
lines = 0
connect = "\\" if dir[-1] == "\\" else "\\\\"

start = time()
for file in listdir(dir):
    with open(f'{dir}{connect}{file}') as f:
        lines = lines + len(f.readlines())
end = time() - start

print(f'{int(end)} 秒。')