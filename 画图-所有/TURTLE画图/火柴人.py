# @Time : 2021/12/12 20:20
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
'''小小爱心火柴人'''
from turtle import *

bgcolor('azure')
pensize(6)
pencolor("yellow")


def hand_leg_color():
    pencolor("pink")
    forward(20)
    pencolor("yellow")


def go_to(x, y):
    up()
    goto(x, y)
    down()


def head(x, y, r):
    pendown()
    go_to(x, y)
    fillcolor("pink")
    begin_fill()
    circle(r)
    end_fill()
    leg(x, y)
    penup()


def leg(x, y):
    right(90)
    forward(100)
    right(45)
    forward(60)
    hand_leg_color()
    go_to(x, y-100)
    left(90)
    forward(60)
    hand_leg_color()
    hand(x, y)


def hand(x, y):
    go_to(x, y-50)
    left(75)
    forward(75)
    left(60)
    hand_leg_color()
    go_to(x, y-50)
    #left(120)
    left(60)
    forward(75)
    #left(60)
    right(60)
    hand_leg_color()
    #left(90)
    right(90)


def big_circle(size):
    speed(0)
    for i in range(100):
        forward(size)
        right(0.45)


def line(size):
    speed(0)
    forward(63 * size)


def small_circle(size):
    speed(0)
    for i in range(180):
        forward(size)
        right(0.917)


def heart(x, y, size):
    go_to(x, y)
    left(120)
    pencolor('red')
    pensize(2)
    fillcolor("pink")
    begin_fill()
    line(size)
    big_circle(size)
    small_circle(size)
    left(120)
    small_circle(size)
    big_circle(size)
    line(size)
    end_fill()


def main():
    head(0, 100, 30)

    head(500, 100, 30)
    right(120)
    heart(150, 50, 1)
    # heart(-150, 50, 1)
    go_to(-195, -150)
    pensize(2)
    write("To: the fairy with wisdom and beauty！", move=True, align="left", font=("华文行楷", 20, "normal"))
    hideturtle()
    done()


main()

