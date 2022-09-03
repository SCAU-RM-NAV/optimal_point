import copy
import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import os,inspect
import yaml

"""
在n个点中计算最优攻击和防御点
输入参数：己方机器人坐标，敌方机器人坐标
输出结果：最优攻击点，最优防御点

"""

class Optimal:
    def __init__(self):
        #self.read_yaml()
        self.obstacle_List = [[12,22,5],[16,28,5],[35,22,5],[39,28,5]]

    #计算最优点
    def calculation_point(self,self_point,enemy_point):
        """
        计算最优点函数
        待完善
        """
        attach_point = []
        defend_point = []

        return attach_point,defend_point


    def distance_of_two_point(self,start,goal):
        """
        参考函数
        计算两点间距离
        """
        return math.sqrt((start[0]-goal[0])**2+(start[1]-goal[1])**2)

    def obstacle_of_two_point(self,start,goal):
        """
        参考函数
        计算两点间障碍物个数
        start、goal分别为线段起点和终点
        全局变量self.obstacle_List为障碍物列表，类初始化时已经定义
        """
        obstacle_num=0
        for (ox, oy, size) in self.obstacle_List:
            dd = self.distance_squared_point_to_segment(
                np.array([start[0], start[1]]),
                np.array([goal[0], goal[1]]),
                np.array([ox, oy]))
            if dd <= size ** 2:
                obstacle_num+=1
                return obstacle_num
        return obstacle_num

    @staticmethod
    def distance_squared_point_to_segment(v, w, p):
        """
        参考函数
        计算两点连线到第三个点距离
        v,w,p为二维数组,本函数返回点p到线段vw距离
        """
        #若两点重合，结果为其中一点到障碍物距离
        if np.array_equal(v, w):
            return (p - v).dot(p - v)  # v == w case
        l2 = (w - v).dot(w - v)  # i.e. |w-v|^2 -  avoid a sqrt
        t = max(0, min(1, (p - v).dot(w - v) / l2))
        projection = v + t * (w - v)  # Projection falls on the segment
        return (p - projection).dot(p - projection)

    
    def draw_graph(self, self_point=None, enemy_point=None,attach_point=None,defend_point=None):
        """
        画图函数
        传入参数：self_point：自身坐标
                enemy_point：敌方坐标
                attach_point：最优攻击点
                defend_point：最优防御点
        """
        plt.clf()
        # for stopping simulation with the esc key.
        plt.gcf().canvas.mpl_connect(
            'key_release_event',
            lambda event: [exit(0) if event.key == 'escape' else None])

        #画自身和敌人位置
        if self_point is not None:
            plt.plot(self_point[0],self_point[1],"8r",ms=10)
        if enemy_point is not None:
            plt.plot(enemy_point[0],enemy_point[1],"8b",ms=10)      

        #画障碍
        for (ox, oy, size) in self.obstacle_List:
            # self.plot_circle(ox, oy, size)
            plt.plot(ox, oy, "ok", ms=10 * size)

        #画最优点
        if attach_point is not None:
            plt.plot(attach_point[0][0],attach_point[0][1],"Dm",ms=10)
        if defend_point is not None:
            plt.plot(defend_point[0][0],defend_point[0][1],"Dy",ms=10)
        plt.axis([0, 50, 0, 50])
        plt.grid(True)
        plt.pause(0.02)
        #plt.show()

def main():
    print("start calculation optimal point!")
    #初始化optimal_point类
    optimal_goal = Optimal()
    for i in range(0,25):
        self_point = [10,45]
        enemy_point = [i,5]
        #attach_point,defend_point,pursuit_point = optimal_goal.calculation_point(self_point=self_point,enemy_point=enemy_point)
        # optimal_goal.draw_graph(self_point,enemy_point,attach_point,defend_point,pursuit_point)
        optimal_goal.draw_graph(self_point,enemy_point,attach_point=None,defend_point=None)

    for i in range(5,45):
        self_point = [10,45]
        enemy_point = [25,i]
        #attach_point,defend_point,pursuit_point = optimal_goal.calculation_point(self_point=self_point,enemy_point=enemy_point)
        # optimal_goal.draw_graph(self_point,enemy_point,attach_point,defend_point,pursuit_point)
        optimal_goal.draw_graph(self_point,enemy_point,attach_point=None,defend_point=None)

    for i in range(25,45):
        self_point = [10,45]
        enemy_point = [i,45]
        #attach_point,defend_point,pursuit_point = optimal_goal.calculation_point(self_point=self_point,enemy_point=enemy_point)
        # optimal_goal.draw_graph(self_point,enemy_point,attach_point,defend_point,pursuit_point)
        optimal_goal.draw_graph(self_point,enemy_point,attach_point=None,defend_point=None)

    for i in range(0,-45,-1):
        self_point = [10,45]
        enemy_point = [45,i+45]
        #attach_point,defend_point,pursuit_point = optimal_goal.calculation_point(self_point=self_point,enemy_point=enemy_point)
        # optimal_goal.draw_graph(self_point,enemy_point,attach_point,defend_point,pursuit_point)
        optimal_goal.draw_graph(self_point,enemy_point,attach_point=None,defend_point=None)

if __name__ == '__main__':
    main()


