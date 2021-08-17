#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as 小写字母
# 从 sys 导入的 maxint 在 64 位系统上太大了
from time import ctime

顶级域名 = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    日期_整数 = randrange(2 ** 31)      # 挑选日期
    日期_字符串 = ctime(日期_整数)        # 日期字符串
    登录_长度 = randrange(4, 8)         # 登录短
    登录 = ''.join(choice(小写字母) for j in range(登录_长度))
    日期_长度 = randrange(登录_长度, 13) # 域名长
    域名 = ''.join(choice(小写字母) for j in range(日期_长度))
    print(f'{日期_字符串}::{登录}@{域名}.{choice(顶级域名)}::{日期_整数}-{登录_长度}-{日期_长度}')