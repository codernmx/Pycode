import turtle
import math

turtle.up()
turtle.goto(-165, -110)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")  # 填充国旗的颜色
turtle.pencolor("red")  # 画笔颜色
turtle.forward(330)  # 长度
turtle.left(90)  # 方向向左转90角
turtle.forward(220)  # 宽度
turtle.left(90)
turtle.forward(330)
turtle.left(90)
turtle.forward(220)
turtle.end_fill()  # 长方形框架画完，此时方向向下
turtle.left(180)  # 把方向转为向上
turtle.up()
turtle.goto(-143, 66)  # 移到大五星最左端的顶点
turtle.down()
turtle.right(90)  # 把方向转为向右
turtle.begin_fill()
turtle.fillcolor("yellow")  # 大五星的颜色
turtle.pencolor("yellow")
for i in range(5):
    turtle.forward(66)  # 大五星的每条边长度
    turtle.right(144)  # 五星的角度为36，所以需要转（180-36）度
turtle.end_fill()  # 大五星画完
turtle.up()
turtle.goto(-110, 55)  # 回到大五星的中心点
# 方向转到大五星中心点到第一个小五星中心点的方向上
turtle.left(math.degrees(math.acos((9 - 25 - 34) / (-2 * 5 * math.sqrt(34)))))
turtle.forward(math.sqrt(55 ** 2 + 33 ** 2) - 11)  # 第一个小五星左边顶点的位置
turtle.left(18)  # 因为刚刚只是转到两个中心点的角度，要画边就需要再左转36/2度
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for i in range(5):
    turtle.forward(math.sin(math.radians(72)) * 11 * 2)  # 画小五星长度
    turtle.right(144)
turtle.end_fill()
turtle.up()
turtle.goto(-110, 55)
turtle.right(18)  # 因为为了画边之前向左转了18度，现在向右返回18度
turtle.right(math.degrees(math.acos((9 - 25 - 34) / (-2 * 5 * math.sqrt(34)))))  # 方向返回水平向右
# 再转到大五星中心点到第二个小五星的中心点方向上
turtle.left(math.degrees(math.acos((1 - 49 - 50) / (-2 * 7 * math.sqrt(50)))))
turtle.forward(math.sqrt(11 ** 2 + 77 ** 2) - 11)
turtle.left(18)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for i in range(5):
    turtle.forward(math.sin(math.radians(72)) * 11 * 2)
    turtle.right(144)
turtle.end_fill()
# 最后的两个小五星的画法同上，就不具体注释
turtle.up()
turtle.goto(-110, 55)
turtle.right(18)
turtle.right(math.degrees(math.acos((1 - 49 - 50) / (-2 * 7 * math.sqrt(50)))))
turtle.right(math.degrees(math.acos((4 - 49 - 53) / (-2 * 7 * math.sqrt(53)))))
turtle.forward(math.sqrt(11 ** 2 + 77 ** 2) - 11)
turtle.left(18)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for i in range(5):
    turtle.forward(math.sin(math.radians(72)) * 11 * 2)
    turtle.right(144)
turtle.end_fill()
turtle.up()
turtle.goto(-110, 55)
turtle.right(18)
turtle.left(math.degrees(math.acos((4 - 49 - 53) / (-2 * 7 * math.sqrt(53)))))
turtle.right(math.degrees(math.acos((16 - 25 - 41) / (-2 * 5 * math.sqrt(41)))))
turtle.forward(math.sqrt(11 ** 2 + 77 ** 2) - 11)
turtle.left(18)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for i in range(5):
    turtle.forward(math.sin(math.radians(72)) * 11 * 2)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
