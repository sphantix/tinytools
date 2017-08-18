#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix
# created time: Mon 24 Jul 2017 03:01:43 PM CST

import os
import os.path
abs_path = os.path.dirname(os.path.abspath(__file__))
case_count = 0

files = os.listdir(abs_path)
for f in sorted(files):
    full_name = os.path.join(abs_path, f)
    if os.path.isdir(full_name) and f != "libs":
        case_count += 1
        print(f)

print("Total case number: {0}".format(case_count))
