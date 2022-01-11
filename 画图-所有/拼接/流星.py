
import tkinter as tk

from time import time, sleep
from random import choice, uniform,randint
from math import sin, cos, radians


# # 初始化tkinter 创建根部件 必须在创建其他部件之前创建 且只有一个
# root = tk.Tk()
# # Label部件
# w = tk.Label(root, text="Hello Tkinter!")
# # pack告诉tkinter调整窗口大小适应所用的小部件
# w.pack()
# root.mainloop()
# 模拟重力
GRAVITY = 0.05
colors = ['red', 'blue', 'pink', 'white', 'green', 'orange', 'purple', 'seagreen', 'indigo', 'cornflowerblue']

class Part(object):
    """
    particles 类
    粒子在空中随机生成，变成一个圈，下坠，消失
    """
    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx=0., vy=0., size=2., color='red', lifespan=2, **kwargs):
        """
        :param cv: 画布
        :param idx: 粒子的id
        :param total: 总数
        :param explosion_speed: 粒子初始速度
        :param x: 粒子的横坐标
        :param y: 粒子的纵坐标
        :param vx: 粒子在x轴上的变化速度
        :param vy: 粒子在y轴上的变化速度
        :param size: 大小
        :param color: 颜色
        :param lifespan: 最高存在时长
        :param kwargs:
        """
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        self.cv = cv
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color
        )
        self.lifespan = lifespan

    def update(self, dt):
        """
        粒子运动函数，膨胀
        :param dt:
        :return:
        """
        self.age += dt
        if self.alive() and self.expand():
            move_x = cos(radians(self.id*360 / self.total)) * self.initial_speed
            move_y = sin(radians(self.id*360 / self.total)) * self.initial_speed
            # self.vy = move_y / (float(dt)*1000)
            self.cv.move(self.cid, move_x, move_y)
            self.vx = move_x / (float(dt) * 1000)

        # 以自由落体坠落
        elif self.alive():
            move_x = cos(radians(self.id*360 / self.total))
            self.cv.move(self.cid, self.vx + move_x, self.vy + GRAVITY*dt)
            self.vy += GRAVITY * dt

        # 移除超过最高时长的粒子
        elif self.cid is not None:
            self.cv.delete(self.cid)
            self.cid = None


    def alive(self):
        """
        检查粒子是否在最高存在时长内
        :return: bool
        """
        return self.age <= 1.2

    def expand(self):
        """
        定义膨胀效果时间帧
        :return: bool
        """
        return self.age <= self.lifespan


def simulate(cv):
    """
    循环调用保持不停
    :param cv: 画布
    :return:
    """
    numb_explode = randint(6, 10)
    wait_time = randint(10, 100)
    explode_points = []
    t = time()
    # 为所有模拟烟花绽放的全部粒子创建一个列表
    for point in range(numb_explode):
        objects = []
        x_cordi = randint(50, 550)
        y_cordi = randint(50, 150)
        speed = uniform(0.5, 1.5)
        size = uniform(1, 3)  # 随机生成一个0.5-3之间的实数
        color = choice(colors)
        explosion_speed = uniform(0.2, 1)
        total_particals = randint(5, 50)
        for i in range(1, total_particals):
            r = Part(cv, idx=1, total=total_particals, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
                     vx=speed, vy=speed ,color=color, size=size, lifespan=uniform(1,0.0005)) #0.6,1.75
            objects.append(r)
        explode_points.append(objects)

    # 设置每个粒子没0.01秒更新状态  生命周期1.8秒  1.6秒存活（1.2秒绽放，0.4秒坠落，0.2秒移除）
    total_time = .0
    # 在1.6秒时间帧内保持更新
    while total_time < 1.8:
        sleep(0.01)
        tnew = time()
        t, dt = tnew, tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    # 循环调用
    root.after(wait_time, simulate, cv)

def close(*ignore):
    """
    退出程序，关闭窗口
    :param ignore:
    :return:
    """
    global root
    root.quit()

if __name__ == '__main__':
    # 初始化tkinter 创建根部件
    root = tk.Tk()

    cv = tk.Canvas(root, height=400, width=600)
    # 绘制一个黑色背景
    cv.create_rectangle(0, 0, 600, 600, fill='black')
    # 使用背景图片
    # image = Image.open('./image.png')
    # photo = ImageTk.PhotoImage(image)
    # cv.create_image(0, 0, image=photo, anchor='nw')
    cv.pack()

    root.protocol('WM_DELETE_WINDOW', close)
    # 1秒后开始条约simulate()
    root.after(10, simulate, cv)
    root.mainloop()