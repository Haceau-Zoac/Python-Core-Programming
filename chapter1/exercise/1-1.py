import re
while True:
    字符串 = input('> ')
    m = re.match(
        # r'.*[bh][aiu]t$'
        r'[bh][aiu]t', 字符串)
    if m is not None:
        print(m.group())