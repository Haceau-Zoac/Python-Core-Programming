#!/usr/bin/env python

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATREST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print(f'ERROR: 无法到达 "{HOST}"')
        return
    print(f'*** 连接到主机 "{HOST}"')

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: 无法登录 anoymously')
        f.quit()
        return
    print('*** 已登录为 "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print(f'ERROR: 无法将目录切换到 "{DIRN}"')
        f.quit()
        return
    print(f'*** 切换到 {DIRN} 目录')

    try:
        f.retrbinary(f'RETR {FILE}',
                open(FILE, 'wb').write)
    except ftplib.error_perm:
        print(f'ERROR: 无法读取文件 "{FILE}"')
        os.unlink(FILE)
    else:
        print(f'*** 已下载 {FILE} 到当前工作目录')
    f.quit()


if __name__ == '__main__':
    main()