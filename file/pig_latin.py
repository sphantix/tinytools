#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

def pig_latin (s):
    vowel = 'AaEeIiOoUu'
    for i, c in s:
        if c in vowel:
            print c, '%d' %i
            continue
        else:
            outs = s[i:] + '-' + s[:i] + 'ay'
            break

    return outs


print pig_latin("three")

