# -*- coding: utf-8 -*-

import sys
import pygame


pygame.init()

size = width, height = 320, 240          # 设置窗口大小

screen = pygame.display.set_mode(size)   # 显示窗口


# 执行死循环
while True:
    # 检查事件
    for event in pygame.event.get():     # 遍历所有事件
        if event.type == pygame.QUIT:    # 如果单击关闭窗口，则推出
            sys.exit()

pygame.quit()  # 推出Pygame










