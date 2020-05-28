# -*- coding:UTF-8 -*-
# AUTHOR: YiJing233
# FILE: D:\Code\Python\pyLab\pyMatplotlib\随机漫步.py
# DATE: 2020/05/29 周五
# TIME: 00:07:58 2020/05/29 周五

# DESCRIPTION: Matplotlib 随机漫步 《Python编程》 p300

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """ 生成一个随机漫步数据的类 """
    def __init__(self, num_points = 5000):
        # 初始化随机漫步属性
        self.nums_points = num_points

        # 起始随机漫步坐标为0
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.nums_points:
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            if x_step == 0 and y_step == 0: 
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.nums_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
        cmap=plt.cm.Blues, edgecolors= 'none',s = 5)
# plt.scatter(0, 0, c='green', edgecolors='none', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.axes().get_xaxis().set_visible(False) # 消除横轴
plt.axes().get_yaxis().set_visible(False) # 消除纵轴

plt.show()