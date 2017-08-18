#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# author : sphantix
# created time: Mon 14 Aug 2017 05:37:46 PM CST

import sys
if len(sys.argv) != 3:
    print("ERROR: 请输入两个需对比的文件名!!!")
    print("USAGE: python3 diff.py file_name1 file_name2")
    sys.exit(1)

file_name_1 = sys.argv[1]
file_name_2 = sys.argv[2]
set1 = set()
set2 = set()

try:
    with open(file_name_1, mode='r') as file1:
        for line in file1:
            set1.add(line.rstrip())
except FileNotFoundError:
    print("Can't find file with name({0}), "
          "please input correct file name!!!".format(file_name_1))
    sys.exit(2)

try:
    with open(file_name_2, mode='r') as file2:
        for line in file2:
            set2.add(line.rstrip())
except FileNotFoundError:
    print("Can't find file with name({0}), "
          "please input correct file name!!!".format(file_name_2))
    sys.exit(2)

print("New Cases:")
for case in list(set1.difference(set2)):
    print(case)
