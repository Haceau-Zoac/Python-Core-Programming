import re
while True:
    字符串 = input('> ')
    m = re.match(
        '[^\s]+@(?:[^\s]+\.)+[^\s]+', 字符串, re.I)
    if m is not None:
        print(m.group())