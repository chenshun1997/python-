#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: ss

import pygame
import sys

# 初始化
pygame.init()

size = width,height = 960,1080 # 设置屏幕尺寸
BLUE = 0,0,255
WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
my_image = pygame.image.load('贵阳地图.png') 
temp = 0
clock = pygame.time.Clock()
# clock_time = clock.tick_busy_loop(60)  #可以用来写延时

# screen = pygame.display.set_mode(size) # 创建surface对象
screen = pygame.display.set_mode(size,0,0)
pygame.display.set_caption('无人机仿真界面') # 创建标题
# 界面备注文字 
font = pygame.font.SysFont("/KhmerOS.ttf", 20)  # 30:font size
text1 = font.render("Desired Location", True, (0,0,0))    # (0,0,0) color of font
text2 = font.render("Current Location", True, (0,0,0)) 





# 圆心位置定义
# position = size[0] // 2 , size[1] // 2
position_exp1 = 430 , 950
position_exp2 = 450 , 950
position_exp3 = 470 , 950
position_exp4 = 490 , 950
position_exp5 = 510 , 950
position_exp6 = 530 , 950


position_cur1 = 430 , 980
position_cur2 = 450 , 980
position_cur3 = 470 , 980
position_cur4 = 490 , 980
position_cur5 = 510 , 980
position_cur6 = 530 , 980

temp_exp1 = position_cur1
temp_exp2 = position_cur2
temp_exp3 = position_cur3
temp_exp4 = position_cur4
temp_exp5 = position_cur5
temp_exp6 = position_cur6

lis1=[temp_exp1,position_exp1]
lis2=[temp_exp2,position_exp2]
lis3=[temp_exp3,position_exp3]
lis4=[temp_exp4,position_exp4]
lis5=[temp_exp5,position_exp5]
lis6=[temp_exp6,position_exp6]
################
# 计算距离

# def error_abs(temp1,temp2):
#     temp_error = temp1-temp2
#     if(temp_error < 0):
#         temp_error=-temp_error
#     else:
#         temp_error=temp_error
#     return temp_error
# # dis1x = 0

def error_abs(temp1,temp2):
    temp_errorx = temp1[0]-temp2[0]
    temp_errory = temp1[1]-temp2[1]
    print(temp_errorx,temp_errory)
    r=(temp_errorx*temp_errorx+temp_errory*temp_errory)**0.5
    return r

dis1=0
moving = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # 获取点击鼠标事件
            if event.button == 1: # 点击鼠标左键
                moving = True
                temp=temp+1
                print(temp)
        if event.type == pygame.MOUSEBUTTONUP: # 获取松开鼠标事件
            if event.button == 1: # 松开鼠标左键
                moving = False
    if moving:
        if temp%6 == 1:
            position_exp1 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置
        if temp%6 == 2:
            position_exp2 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置
        if temp%6 == 3:
            position_exp3 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置
        if temp%6 == 4:
            position_exp4 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置
        if temp%6 == 5:
            position_exp5 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置
        if temp%6 == 0:
            position_exp6 = pygame.mouse.get_pos() # 更新圆心位置为鼠标当前位置   
        # print(position)
        if position_exp1 != temp_exp1:
            lis1.append(position_exp1)
            print(lis1)
            # print(lis1)
            dis1= error_abs(position_exp1,temp_exp1) 
            print(dis1)



            
            temp_exp1 = position_exp1
        if position_exp2 != temp_exp2:
            lis2.append(position_exp2)
            print(lis2)
            temp_exp2 = position_exp2
        if position_exp3 != temp_exp3:
            lis3.append(position_exp3)
            print(lis3)
            temp_exp3 = position_exp3
        if position_exp4 != temp_exp4:
            lis4.append(position_exp4)
            print(lis4)
            temp_exp4 = position_exp4
        if position_exp5 != temp_exp5:
            lis5.append(position_exp5)
            print(lis5)
            temp_exp5 = position_exp5
        if position_exp6 != temp_exp6:
            lis6.append(position_exp6)
            print(lis6)
            temp_exp6 = position_exp6


    if(dis1<2):
        position_cur1=position_exp1
    else:
        position_cur1=((position_cur1[0]+(position_exp1[0]-position_cur1[0])/1000),(position_cur1[1]+(position_exp1[1]-position_cur1[1])/1000))
    # screen.fill(WHITE) # 填充屏幕
    screen.blit(my_image, (0, 0))
    screen.blit(text1,(840,8))
    screen.blit(text2,(840,36))
    # 画障碍 BLUE
    pygame.draw.circle(screen,BLUE,(400,500),30)
    pygame.draw.circle(screen,BLUE,(600,500),30)


    # 画轨迹线
    pygame.draw.aalines(screen, BLACK,False,lis1,1)
    pygame.draw.aalines(screen, BLACK,False,lis2,1)
    pygame.draw.aalines(screen, BLACK,False,lis3,1)
    pygame.draw.aalines(screen, BLACK,False,lis4,1)
    pygame.draw.aalines(screen, BLACK,False,lis5,1)
    pygame.draw.aalines(screen, BLACK,False,lis6,1)


    # (text,(10,10))
    # 画期望的圆
    pygame.draw.circle(screen,RED,(828,15),6)
    pygame.draw.circle(screen,RED,position_exp1,8)
    pygame.draw.circle(screen,RED,position_exp2,8)
    pygame.draw.circle(screen,RED,position_exp3,8)
    pygame.draw.circle(screen,RED,position_exp4,8)
    pygame.draw.circle(screen,RED,position_exp5,8)
    pygame.draw.circle(screen,RED,position_exp6,8)
    # pygame.draw.circle(screen, BLACK, position, 50, 1)
    # pygame.draw.circle(screen, RED, position, 80, 1)
    # pygame.draw.circle(screen, GREEN, position, 120, 1)
    # 画当前位置的圆
    pygame.draw.circle(screen,GREEN,(828,42),6)
    pygame.draw.circle(screen,GREEN,position_cur1,8)
    pygame.draw.circle(screen,GREEN,position_cur2,8)
    pygame.draw.circle(screen,GREEN,position_cur3,8)
    pygame.draw.circle(screen,GREEN,position_cur4,8)
    pygame.draw.circle(screen,GREEN,position_cur5,8)
    pygame.draw.circle(screen,GREEN,position_cur6,8)






























    # 刷新屏幕
    pygame.display.update()
    # pygame.display.flip()