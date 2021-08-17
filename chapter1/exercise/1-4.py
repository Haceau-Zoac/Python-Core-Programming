import re
while True:
    字符串 = input('> ')
    m = re.match(
        r'[^\d\s\[\]\{\};:\'"\?/\\><,.!@#$%^&\*\(\)-+=]+[^\s\[\]\{\};:\'"\?/\\><,.!@#$%^&\*\(\)-+=]*', 字符串)
    if m is not None:
        print(m.group())