import re
while True:
    字符串 = input('> ')
    m = re.match(
        # r'[A-Za-z]+, [A-Za-z]+'
        r'[A-Za-z]+, [A-Za-z]', 字符串)
    
    if m is not None:
        print(m.group())