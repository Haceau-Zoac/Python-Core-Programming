import re
while True:
    字符串 = input('> ')
    m = re.match('[-+]?(?:[A-Za-z-]+://)?www\.[A-Za-z_-]+\.(?:com|edu|net)/?', 字符串)
    if m is not None:
        print(m.group())