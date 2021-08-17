#!/usr/bin/env python

import nntplib
import socket

HOST = 'web.aioe.org'
GRNM = 'comp.lang.python'

def main():
    try:
        n = nntplib.NNTP(HOST)
    except socket.gaierror as e:
        print(f'ERROR: 无法到达主机 "{HOST}"')
        print(f'    ("{eval(str(e))[1]}")')
        return
    except nntplib.NNTPPermanentError as e:
        print(f'ERRPR: 在 "{HOST}" 的访问被拒绝')
        print(f'    ("{str(e)}")')
    print(f'*** 连接到主机 "{HOST}"')

    try:
        _, _, _, lst, _ = n.group(GRNM)
    except nntplib.NNTPTemporaryError as ee:
        print(f'ERROR: 无法加载组 "{GRNM}"')
        print(f'    ("{str(ee)}")')
        print('    服务器可能需要身份验证')
        print('    上面的未注销/编辑登录行')
        n.quit()
        return
    except nntplib.NNTPTemporaryError as ee:
        print(f'ERROR: 组 "{GRNM}" 不可用')
        print(f'    ("{str(ee)}")')
        n.quit()
        return
    print(f'*** 找到新闻组 "{GRNM}"')

    rng = f'{lst}-{lst}'
    _, frm = n.xhdr('from', rng)
    _, sub = n.xhdr('subject', rng)
    _, dat = n.xhdr('date', rng)
    print(f'''*** 找到最近文章 (#{lst})
    
    来自：{frm[0][1]}
    主题：{sub[0][1]}
    日期：{dat[0][1]}
''')

    _, data = n.body(lst)
    displayFirst20(data.lines)
    n.quit()

def displayFirst20(data):
    print('*** 有意义的行（<= 20）：\n')
    count = 0
    lines = (line.decode().rstrip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not \
                lower.startswith('>>>') or \
                lower.startswith('|') or \
                lower.startswith('in article') or \
                lower.endswith('writes:') or \
                lower.endswith('wrote:')):
                    continue
        if not lastBlank or (lastBlank and line):
            print(f'    {line}')
            if line:
                count += 1
                lastBlank = False
            else:
                lastBlank = True
        if count == 20:
            break

if __name__ == '__main__':
    main()