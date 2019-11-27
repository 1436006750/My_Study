# coding:utf-8

import re

print(re.match('www', 'www.runoob.com').span())  # 在起始位置开始匹配

print(re.match('com', 'www.runoob.com'))         # 不在起始位置开始匹配


"""     输出结果:
                (0, 3)
                None
"""




