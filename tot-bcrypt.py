#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bcrypt decode single
# Open Source Dedoce gagaltotal666 - Tot

from passlib.hash import bcrypt
from libsrary import pingo
import os
import sys
import color

print ("\n")
print ("=============================   Welcome To Tot-bcrypt       ===========================")
print ("=   ████████╗ ██████╗ ████████╗   ██████╗  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗  =")
print ("=   ╚══██╔══╝██╔═══██╗╚══██╔══╝   ██╔══██╗██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝  =")
print ("=      ██║   ██║   ██║   ██║█████╗██████╔╝██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║     =")
print ("=      ██║   ██║   ██║   ██║╚════╝██╔══██╗██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║     =")
print ("=      ██║   ╚██████╔╝   ██║      ██████╔╝╚██████╗██║  ██║   ██║   ██║        ██║     =")
print ("=      ╚═╝    ╚═════╝    ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝     =")
print ("============================= https://gagaltotal.github.io/ ===========================")
print ("\n")

options = input('decode bcrypt nya bro ? ketik (y) untuk melanjutkan decode, key (ctrl+c) tidak melanjutkan decode : ')

if (options != "y" and options != "n"):
    sys.exit('Invalid Option')

passwords = (options == "y")
text_file = open("worldlist.txt", "r")

words = text_file.read().splitlines()

hash = input('masukan hash bcrypt : ')
length = len(words)

correct_word = ""
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Tunggu Sebentar :', suffix='Complete')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        print()
        break

print("Hasil Decode Bcrypt :", correct_word)
