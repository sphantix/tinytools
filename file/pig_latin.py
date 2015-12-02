#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author : sphantix

VOWELS = ('A','a','E','e','I','i','O','o','U','u')

def convert_word (word):
    i = 0
    for c in word:
        if c not in VOWELS:
            i+=1
            continue
        else:
            outs = word[i:] + '-' + word[:i] + 'ay'
            break

    return outs

def convert_sentence(sentence):
    words = sentence.split(' ')
    new_sentence = ""
    for word in words:
        new_sentence = new_sentence + convert_word(word)
        new_sentence = new_sentence + " "
    return new_sentence.strip()

def convert_word_back(word):
    words = word.split('-')
    new_word = ''.join([words[1][:-2], words[0]])
    return new_word

def convert_sentence_back(sentence):
    words = sentence.split(' ')
    new_sentence = ""
    for word in words:
        new_sentence = new_sentence + convert_word_back(word)
        new_sentence = new_sentence + " "
    return new_sentence

origin_sentence = "Now, let's write the main program code, to ask the user and convert."

converted_sentence = convert_sentence(origin_sentence)
converted_back_sentence = convert_sentence_back(converted_sentence)

print "origin_sentence = %s" %origin_sentence
print "converted_sentence = %s" %converted_sentence
print "converted_back_sentence = %s" %converted_back_sentence
