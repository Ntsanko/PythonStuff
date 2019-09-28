# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:52:25 2019

@author: Ntsanko

"""

# Hint of the challenge is one small letter surrounded by exactly 3 big ones.
# While the Hint itself was... incomplete, the image accompanying gave more about the clue

import re

text = open('level_3.txt').read()
answer = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", text))
print(answer)



