# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:24:11 2019

@author: Ntsanko
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:24:11 2019

@author: Ntsanko
"""

import requests
from bs4 import BeautifulSoup
from bs4 import Comment
from collections import Counter

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
texts = []
for c in comments:
    texts.append(c.extract())
  
counter = Counter(texts[1]).most_common()
counter_list =list(sum(counter, ()))
unique = ""
for char in counter_list:
    char = str(char)
    if char.isalpha():
        unique += char
print(unique)



