import turtle
from turtle import *
speed(100)  # 速度
#
#
#
color('black')  # 黑色
pensize(2)  # 画笔粗细

right(60)  # 左旋转45


# 画嘴巴
penup()
goto(-300, 50)
down()
circle(300, 120)  # 半圆 半径40

right(120)  # 左旋转45
circle(200, -20)  # 半圆 半径40
right(-180)  # 左旋转45
circle(237, 160)  # 半圆 半径40
right(185)  # 左旋转45
circle(200, -20)  # 半圆 半径40

# t.penup()


def draw_flower(x, y, radius, extent, n, color):
    '''
    :param x: 花的起点横坐标
    :param y: 花的起点纵坐标
    :param radius: 半径
    :param extent: 弧度
    :param n: 花瓣的个数
    :param color: 填充的颜色
    :return:
    '''
    degree = 360 / n
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.setheading(i * degree)
        turtle.circle(radius, extent)
        turtle.left(180 - extent)
        turtle.circle(radius, extent)
    turtle.end_fill()


# if __name__ == "__main__":
    # turtle.Screen().setup(width=800, height=600, startx=0, starty=0)
    # hideturtle()
    # # up()
    # # goto(-260, 270)
    # # write("头条cloudcoder出品", align='left', font=('fangsong', 14, 'normal'))
    # showturtle()
    # #
    # # speed(20)
    # bgcolor("white")
    # # pensize(1)


pencolor("")
# draw_flower(-200, 150, 100, 80, 4, 'red')
# draw_flower(-200, -150, 100, 90, 5, 'purple')
draw_flower(-230, 160, 90, 95, 5, 'pink')
# draw_flower(200, -150, 110, 100, 4, 'yellow')
done()  # 保持不关闭
