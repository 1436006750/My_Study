# -*- coding: utf-8 -*-

import pygame
import sys
import random


class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        self.bird_Rect = pygame.Rect(65, 50, 50, 50)  # 鸟的矩形
        # 定义鸟的3种状态列表
        self.bird_Status = [pygame.image.load("Picture/bird.png"),
                            pygame.image.load("Picture/bird.png"),
                            pygame.image.load("Picture/bird.png")]

        self.status = 0       # 默认飞行状态
        self.bird_X = 120
        self.bird_Y = 350
        self.jump = False     # 默认情况下，小鸟自动降落
        self.jump_Speed = 10  # 跳跃高度
        self.gravity = 5      # 重力
        self.dead = False     # 默认小鸟生命状态---活着
        # pass

    def bird_Update(self):
        if self.jump:
            # 小鸟跳跃
            self.jump_Speed -= 1  # 速度递减--上升速度越来越慢
            self.bird_Y -= self.jump_Speed  # 小鸟 Y轴坐标减小----上升
        else:
            # 小鸟降落
            self.gravity += 0.2   # 重力作用下，下降速度越来越快
            self.bird_Y += self.gravity     # 小鸟 Y轴坐标增加----下降
        self.bird_Rect[1] = self.bird_Y     # 更改 Y轴坐标
        # pass


class Pipe_line(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        self.wallx = 400                        # 加载管道所在 X轴坐标
        self.pine_Up = pygame.image.load("Picture/pipeline.jpeg")    # 加载 上方 管道图片
        self.pine_Down = pygame.image.load("Picture/pipeline.jpeg")  # 加载 下方 管道图片
        # pass

    def update_Pipeline(self):
        """管道移动方法：水平移动"""
        self.wallx -= 5    # 管道的X轴坐标递减，即管道向坐移动

        # 当管道运行到一定位置的时候-----即小鸟飞跃管道----分数+1,并且重置管道
        if self.wallx < -80:
            global score
            score += 1
            self.wallx = 400
        # pass


def create_Map():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # 显示管道
    screen.blit(Pipe_line.pine_Up, (Pipe_line.wallx, -300))   # 上管道坐标为位置
    screen.blit(Pipe_line.pine_Down, (Pipe_line.wallx, 500))  # 下管道坐标位置
    Pipe_line.update_Pipeline()                               # 管道移动

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2   # 撞管道状态
    elif Bird.jump:
        Bird.status = 1   # 起飞状态
    # 设置小鸟坐标
    screen.blit(Bird.bird_Status[Bird.status], (Bird.bird_X, Bird.bird_Y))
    Bird.bird_Update()  # 鸟---移动

    # 显示分数
    screen.blit(font.render(str(score), -1, (255, 255, 255)), (200, 50))  # 设置颜色以及坐标位置

    pygame.display.update()


def check_Dead():
    # 上方管道的矩形位置
    up_Rect = pygame.Rect(Pipe_line.wallx, -300,
                          Pipe_line.pine_Up.get_width() - 10,
                          Pipe_line.pine_Down.get_height())
    # 下方管道的矩形位置
    down_Rect = pygame.Rect(Pipe_line.wallx, 500,
                            Pipe_line.pine_Up.get_width() - 10,
                            Pipe_line.pine_Down.get_height())
    # 检测小鸟与上下方管道是否碰撞
    if up_Rect.colliderect(Bird.bird_Rect) or down_Rect.colliderect(Bird.bird_Rect):
        Bird.dead = True
        return True
    else:
        return False


def get_Result():
    final_text1 = "Game Over"
    final_text2 = "you final score is: " + str(score)

    ft1_font = pygame.font.SysFont("Arial", 70)            # 设置第一行文字字体
    ft1_surf = font.render(final_text1, 1, (242, 3, 36))   # 设置第一行文字颜色
    ft2_font = pygame.font.SysFont("Arial", 50)
    ft2_surf = font.render(final_text2, 1, (255, 177, 6))  #
    # 设置第一行文字的显示位置
    screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 200])
    # 设置第二行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])

    pygame.display.flip()    # 更新整个待显示的 Surface对象到屏幕上
    

# 不要再写错了, 是(name = main)
if __name__ == '__main__':
    """主程序"""
    pygame.init()
    pygame.font.init()                      # 初始化字体
    font = pygame.font.SysFont(None, 50)    # 设置默认字体和大小
    size = width, height = 400, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipe_line = Pipe_line()                 # 实例化管道
    Bird = Bird()                           # 实例化鸟类
    score = 0                               # 初始化分数
    while True:
        clock.tick(60)
        # 轮寻事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True       # 跳跃
                Bird.gravity = 5       # 重力
                Bird.jump_Speed = 10   # 跳跃速度

        background = pygame.image.load("Picture/background.jpg")

        if check_Dead():
            get_Result()
        else:
            create_Map()

    pygame.quit()











