#!/usr/bin/env python3
# -*- coding: gbk -*-
# author : sphantix
# created time: Fri 10 Feb 2017 02:31:16 PM CST

import sys

output_file = sys.argv[1] + '.out'

with open(output_file, mode='w') as outf:
    with open(sys.argv[1], mode='r', encoding='gbk', errors='ignore') as inf:
        for line in inf:
            outf.write(line)
