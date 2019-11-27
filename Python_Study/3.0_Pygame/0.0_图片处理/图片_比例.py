# -*- coding: utf-8 -*-

from __future__ import print_function   # syntaxerror:从\未来\导入必须发生在文件的开头
from PIL import Image


# 源文件------图片
Picture_File = '/root/zx/3.0_Personal_Study/Pygame/2.0_Flappy_Bird/Picture/bird1.jpg'


# 打开图片，即实例化----可以通过对象操作图像
im = Image.open(Picture_File)
print(im.format, im.size, im.mode)

"""
/usr/bin/python2.7 /root/zx/3.0_Personal_Study/Pygame/0.0_图片处理/图片_比例.py
JPEG (660, 406) RGB
"""

im.show()  # 显示刚才加载的图片


# 创建图片的缩略图---并保存到指定的目录下
size = (100, 50)
im.thumbnail(size)
im.save("../2.0_Flappy_Bird/Picture/bird.png", "PNG")  # 以png格式保存缩略图， 保存到某个路径下


