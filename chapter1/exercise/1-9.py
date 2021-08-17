import re
while True:
    字符串 = input('> ')
    m = re.match('[-+]?\d+\.(?:\d+(?:e[-+]?\d+)?)?', 字符串, re.I)
    if m is not None:
        print(m.group())