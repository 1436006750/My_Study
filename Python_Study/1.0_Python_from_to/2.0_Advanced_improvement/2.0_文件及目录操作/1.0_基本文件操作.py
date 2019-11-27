# -*- coding: utf-8 -*-


filename_ = 'test.txt'         # 文件名
model_ = 'a+'                   # 打开方式---追加模式
# file = open(filename_, model_)


# 升级版 ---打开文件(可读写)
with open(filename_, model_) as file:

    # 写入文本
    string_ = "向文本中写入数据"
    file.write(string_)

    # 移动文件流     0--开头，  1--现在位置， 2--结尾    (必须填写参数)
    file.seek(0)

    # -------------------------------读取文件-----------------------
    # 读取指定字符---默认则读取全部
    string_read = file.read()
    print("读取全部： ", string_read)

    file.seek(0)

    # 读取一行
    string_readline = file.readline()
    print('读取一行： ', string_readline)

"""
注意：文件流问题，追加打开的文件流在文件尾部
     这样的话，一些操作无法正常进行 ---------- 读
"""





