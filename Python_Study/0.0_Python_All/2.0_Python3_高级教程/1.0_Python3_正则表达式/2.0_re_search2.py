# coding:utf-8


import re


line = "Cats are smarter than dogs"

search_obj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if search_obj:
    print("search_obj.group()  : ", search_obj.group())
    print("search_obj.group(1) : ", search_obj.group(1))
    print("search_obj.group(2) : ", search_obj.group(2))
else:
    print("Nothing found!!")


"""
search_obj.group()  :  Cats are smarter than dogs
search_obj.group(1) :  Cats
search_obj.group(2) :  smarter
"""


