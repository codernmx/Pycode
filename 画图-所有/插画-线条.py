import time
import turtle as t

t.penup()
t.speed(20)
t.hideturtle()  # 影藏最终箭头
t.screensize(400, 800, "#0D153A")
t.goto(0, 310)
t.color('white')
t.write('BUCT', font=("Arial", 34, "normal"), align='center')
t.goto(0, 280)
t.write('握住此生辽阔，赠你漫天星火。', font=("Arial", 18, "normal"), align='center')
t.goto(0, 250)
t.write('北化播散属于你的希望!', font=("Arial", 15, "normal"), align='center')

t.goto(-60, 120)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-160, 50)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-15, 135)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-150, 35)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-5, 120)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-140, 20)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-200, 20)
t.begin_fill()
for _ in range(5):  # 重复执行5次
    t.forward(50)  # 向前移动200步
    t.right(144)  # 向右移动144度，注意这里的参数一定不能变
t.end_fill()  # 结束填充红色
# time.sleep(1)


# 中间的星星
t.goto(-110, -30)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-210, -100)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-65, -15)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-200, -115)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-55, -30)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(-190, -130)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(-250, -130)
t.begin_fill()
for _ in range(5):  # 重复执行5次
    t.forward(50)  # 向前移动200步
    t.right(144)  # 向右移动144度，注意这里的参数一定不能变
t.end_fill()  # 结束填充红色

# 右边的星星
t.goto(140, 70)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(40, 0)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(185, 85)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(50, -15)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(195, 70)  # 落到坐标轴为(-300, 0)的位置
t.pendown()  # 落下画笔，开始绘制
t.goto(60, -30)  # 到坐标轴为(50, 0)的位置
t.penup()

t.goto(0, -30)
t.begin_fill()
for _ in range(5):  # 重复执行5次
    t.forward(50)  # 向前移动200步
    t.right(144)  # 向右移动144度，注意这里的参数一定不能变
t.end_fill()  # 结束填充红色
time.sleep(1)

t.pensize(2)
t.goto(250, -130)
t.pendown()  # 落下画笔，开始绘制
t.goto(190, -80)  # 到坐标轴为(50, 0)的位置
t.goto(-50, -170)  #
t.goto(-50, -400)  #
t.goto(200, -370)  #
t.goto(250, -400)  #
t.goto(200, -370)  # 回去
t.goto(200, -280)  #
t.goto(250, -310)  #
t.goto(200, -280)  # 回  折拐点
t.goto(-50, -310)  #
# 画方块
t.goto(-50, -300)  #
t.goto(200, -270)
# t.goto(200 ,-280)
t.goto(250, -300)  #
t.goto(200, -270)  # 回到中间
t.goto(190, -80)  # 到上方

t.write('图书馆', font=("Arial", 13, "normal"), align='center')
# t.write('LIBRARY',font=("Arial" , 13 , "normal"),align='center')


# 图书馆中间的线条
t.penup()

t.goto(-50, -190)  #
t.pendown()  # 落下画笔，开始绘制

t.goto(140, -120)  #
t.penup()
t.goto(-50, -200)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(110, -140)  #
t.penup()

t.goto(-50, -205)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(120, -140)  #
t.penup()

t.goto(-50, -235)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(100, -180)  #
t.penup()

t.goto(-50, -245)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(150, -170)  #

t.penup()
t.goto(-50, -275)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(100, -230)  #
t.penup()

t.goto(-50, -285)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(150, -230)  #


def draw_rec(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.color('white')
    t.goto(x, y - 10)
    t.goto(x + 10, y - 10)
    t.goto(x + 10, y)
    t.goto(x, y)
    t.end_fill()
    t.pu()


y = -300
x = - 50
for item in range(0, 13):
    draw_rec(x, y)
    y += 3 - 0.1 * item
    x += 20


def draw_line(x, y, w, h):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.goto(x + w, y + h)
    t.pu()


line_list = [[-50, -330, 246, 30], [-50, -390, 246, 30], [100, -310, 0, -60], [-50, -340, 80, 10]
             , [-50, -370, 130, 10], [200, -340, -60, 10], [200, -350, -30, 10], [200, -370, -40, 10]
             , [100, -310, -10, 0], [100, -330, -30, 0]]
for item in line_list:
    draw_line(item[0], item[1], item[2], item[3])

t.penup()

t.goto(250, -140)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(200, -100)  #

t.penup()

t.goto(250, -170)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(200, -130)  #

t.penup()

t.goto(250, -210)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(200, -170)  #


t.penup()

t.goto(250, -250)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(200, -210)  #

t.penup()

t.goto(250, -350)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(220, -330)  #

t.penup()

t.goto(220, -300)  #
t.pendown()  # 落下画笔，开始绘制
t.goto(220, -370)  #

t.done()
