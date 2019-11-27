# -*- coding: utf-8 -*-


import sys
import pygame


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (0, 0, 0)


ball = pygame.image.load("ball.jpg")
ball_rect = ball.get_rect()           # 获取矩形区域


speed = [5, 5]  # 设置移动的X轴 Y轴距离

clock = pygame.time.Clock()  # 实例化一个时钟
# 执行死循环，确保窗口一直显示
while True:
    clock.tick(60)  # 每秒60次
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)  # 移动小球
    # 碰到左右边缘
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)            # 上色
    screen.blit(ball, ball_rect)  # 将图片画到窗口上
    pygame.display.flip()         # 跟新全部显示

pygame.quit()









