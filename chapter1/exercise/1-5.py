import re
while True:
    字符串 = input('> ')
    m = re.match('\d+ (?:[A-Za-z]+ ?)+', 字符串)
    if m is not None:
        print(m.group())