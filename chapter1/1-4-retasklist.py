#!/use/bin/env python

import os
import re

with os.popen('tasklist /nh', 'r') as 文件:
    for 某行 in 文件:
       print(re.findall(
            r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
            某行.rstrip()))