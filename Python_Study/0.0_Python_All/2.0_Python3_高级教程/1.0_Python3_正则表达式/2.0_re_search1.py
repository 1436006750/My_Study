# coding:utf-8

import re


print(re.search('www', 'www.runoob.com').span())   # 在起始的位置匹配

print(re.search('com', 'www.runoob.com').span())   # 不在起始的位置匹配


"""         输出结果：
                    (0, 3)
                    (11, 14)
"""




