import re
while True:
    字符串 = input('> ')
    m = re.match('[-+]?(?:0[box]?)?[\dA-Fa-f]+', 字符串, re.I)
    if m is not None:
        print(m.group())