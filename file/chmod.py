#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# author : sphantix
# created time: Mon 14 Aug 2017 09:07:05 AM CST

import os

rootdir = os.path.dirname(os.path.abspath(__file__))


def change_file_name(origin_name):
    replace_name = origin_name.replace(" ", "\ ").replace("[", "\[").replace("]", "\]").replace("(", "\(").replace(")", "\)").replace("'", "\'").replace("&", "\&")
    # if not replace_name == origin_name:
    #     cmd = "sudo mv {0} {1}".format(
    #         os.path.join(parent, origin_name.replace(" ", "\ ")),
    #         os.path.join(parent, replace_name))
    #     print(cmd)
    #     os.system(cmd)

    return replace_name


def chmod(abs_file_name, is_directory):
    cmd = None
    if is_directory:
        cmd = "sudo chmod 775 {0}".format(abs_file_name)
    else:
        cmd = "sudo chmod 666 {0}".format(abs_file_name)

    print(cmd)
    os.system(cmd)


for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        chmod(os.path.join(parent, change_file_name(dirname)), True)

    for filename in filenames:
        chmod(os.path.join(change_file_name(parent),
                           change_file_name(filename)), False)
