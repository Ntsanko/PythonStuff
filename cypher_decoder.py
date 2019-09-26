# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:45:53 2019

@author: Ntsanko
"""
##had no idea of the existence of special functions here
key_string = "abcdefghijklmnopqrstuvwxyz"
special_string = "().' "
last_letters = "yz"
key_step = 2
coded_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
translated_string = ""
for char in coded_string:
    if char in special_string:
        translated_string += char
    else:
        if char in last_letters:
            translated_string += key_string[last_letters.index(char)]
        else:
            translated_string += key_string[key_string.index(char)+2]
        
print(translated_string)
##Second solution after reading translation
print("=============")
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = 'cdefghijklmnopqrstuvwxyzab'
dict = str.maketrans(str1, str2)
print(coded_string.translate(dict))
print("=========")
##Moving on to the next level
print("Solution for next level")
print("map".translate(dict))


97999810099101