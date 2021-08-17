#!/use/bin/env python

import os
from distutils.log import warn as 输出
import re

with os.popen('who', 'r') as 文件:
    for 某行 in 文件:
        输出(re.split(r'\s\s+|\t', 某行.strip()))