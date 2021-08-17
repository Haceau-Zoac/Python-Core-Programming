import re
while True:
    字符串 = input('> ')
    m = re.match(
        '[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)? *[+-] *[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?j', 字符串, re.I)
    if m is not None:
        print(m.group())