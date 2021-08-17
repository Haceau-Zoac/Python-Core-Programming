#!/usr/bin/env python

import os
import re

with os.popen('who', 'r') as 文件:
    for 某行 in 文件:
        print(re.split(r'\s\s+|\t', 某行.strip()))