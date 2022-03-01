import turtle as t

t.color('black')  # 黑色
t.pensize(8)  # 画笔粗细

t.penup()  # 提起画笔
t.goto(60, 0)
t.down()
t.left(45)  # 左旋转45
t.circle(120, 270)

# 画眼珠子
def drawEye(x, y):
    t.penup()
    t.goto(x, y)  # 移动 到开始画眼珠子的点
    t.down()
    t.begin_fill()  # 开始填充颜色
    t.circle(16)
    t.end_fill()  # 填色


def eye(x, y):
    t.penup()
    t.goto(x, y)  # 移动 到开始画框框（椭圆）
    t.down()
    for i in range(2):  # 将相同的动作重复做一遍（两次一半一次）
        for j in range(9):
            t.forward(j)
            t.left(10)
        for j in range(9, 0, -1):
            t.forward(j)
            print(j)
            t.left(10)


t.right(45)  # 左旋转45
eye(10, 100)  # 右眼
drawEye(28, 100)  # 右眼竹子
eye(-120, 100)  # 左眼
drawEye(-102, 100)  # 左眼珠子

# 画嘴巴
t.penup()
t.goto(-60, 50)
t.down()
t.circle(40, 180)  # 半圆 半径40

t.penup()
t.goto(-130, 20)
t.down()
t.circle(30)  # 圆（手那一部分）

t.penup()
t.goto(-155, 40)  # 中指的起点
t.down()
t.goto(-155, 80)  # 中指的最上顶点

t.penup()
t.down()
t.circle(8, 180)  # 中指上半圆
t.goto(-171, 40)

t.done()  # 保持不关闭
