# -*- coding: utf-8 -*-

import os

print(os.name)
# posix:表示Linux系统


# 相对路径
print(os.getcwd())
# /root/zx/3.0_Personal_Study/1.0_Python_from_to/2.0_Advanced_improvement/2.0_文件及目录操作


# 绝对路径
print(os.path.abspath("test.txt"))
# /root/zx/3.0_Personal_Study/1.0_Python_from_to/2.0_Advanced_improvement/2.0_文件及目录操作/test.txt


# 判断目录是否存在
print(os.path.exists("test.txt"))    # True
print(os.path.exists("./test.txt"))  # True


# 创建目录
path_1 = './test'
if os.path.exists(path_1):
    print('该目录已存在,无法再创建！')
else:
    os.mkdir(path_1, mode=0o777)


# 创建多级目录
path_2 = './test1/test11'
if os.path.exists(path_2):
    print('该目录已存在,无法再创建！')
else:
    os.mkdir(path_2, mode=0o777)


# 删除目录-----目录不存在，会出异常
if os.path.exists(path_1):
    os.rmdir(path_1)
    print("rmdir :删除目录成功!", path_1)
else:
    print("删除目录失败，目录不存在！")


# 遍历目录
# path_3 = '../../../1.0_Python_from_to'
# tuples = os.walk(path_3)
# for tuple1 in tuples:
# #   print(tuple1, '\n')

# 删除文件------------不能
path_3 = './test1'
if os.path.exists(path_3):
    # os.remove(path_3)
    print('remove :文件删除成功!')
else:
    print('文件不存在，删除失败！')


# 获取文件信息
print(os.stat(path_3))












