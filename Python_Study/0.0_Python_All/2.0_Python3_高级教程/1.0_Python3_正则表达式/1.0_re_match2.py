# coding:utf-8

import re

line = "Cats are smarter then dogs"

# .*表示任意匹配除换行符(\n  \r)之外的任何单个或者多个字符
match_obj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if match_obj:
    print("match_obj.group()  : ", match_obj.group())
    print("match_obj.group(1) : ", match_obj.group(1))
    print("match_obj.group(2) : ", match_obj.group(2))
else:
    print("No match!!")


"""          输出结果：
                     match_obj.group()  :  Cats are smarter then dogs
                     match_obj.group(1) :  Cats
                     match_obj.group(2) :  smarter
"""





