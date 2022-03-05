import turtle as t

t.pensize(5)
t.pencolor('black')
t.speed(10)
t.bgcolor('skyblue')


def draw_bat():
    t.pu()  # 起笔
    t.goto(-300, 200)  # 将画笔移动到指定位置
    t.pd()  # 落笔
    t.begin_fill()
    t.color('yellow')
    t.circle(radius=50)  # radius半径属于circle函数、类型为float型
    t.end_fill()
    t.pu()

    t.goto(0, 0)
    # 小兔的面部
    t.pd()
    t.color('pink')
    t.pensize(5)  # 画笔宽度
    t.circle(radius=100)  # 脸
    # 眼睛
    t.pencolor('black')
    # 左眼
    t.pu()  # 起笔
    t.goto(-45, 92)  # 将画笔移动到指定位置
    t.pd()  # 落笔
    t.begin_fill()
    t.color((0, 0, 0), (0, 0, 0.1))
    t.circle(radius=10)  # radius半径属于circle函数、类型为float型
    # 右眼
    t.pu()
    t.goto(45, 92)
    t.pd()
    t.circle(radius=10)
    t.end_fill()

    # 鼻子
    t.pu()
    t.goto(20, 60)
    t.color('pink')
    t.pd()
    t.begin_fill()
    t.goto(-20, 60)
    t.goto(0, 45)
    t.goto(20, 60)
    t.end_fill()
    # 嘴
    t.goto(0, 45)
    t.goto(0, 40)
    t.seth(-90)  # 画笔朝向角度
    t.circle(10, 120)  # 画笔圆的半径及其画圆的弧度
    t.pu()
    t.goto(0, 40)
    t.seth(-90)
    t.pd()
    t.circle(-10, 120)
    # 小兔的耳朵
    # 左耳
    t.pu()
    t.goto(-60, 180)  #
    t.seth(200)
    t.pd()
    t.circle(radius=200, extent=90)
    t.goto(-98, 110)

    # 右耳
    t.pu()
    t.goto(60, 180)  #
    t.seth(-20)
    t.pd()
    t.circle(radius=-200, extent=90)
    t.goto(98, 110)
    # 小兔的身体
    t.pu()
    t.goto(20, 3)
    t.seth(-25)
    t.pd()
    t.circle(radius=-250, extent=25)
    t.circle(radius=-135, extent=260)
    t.seth(50)
    t.circle(radius=-250, extent=25)
    ##小兔的胳膊
    # 左臂
    t.pu()
    t.seth(180)
    t.goto(-30, -3)
    t.pd()
    # 胳膊
    t.circle(radius=248, extent=30)
    t.circle(radius=29, extent=185)
    # 右臂
    t.pu()
    t.seth(0)
    t.goto(30, -3)
    t.pd()
    t.circle(radius=-248, extent=30)
    t.circle(radius=-27, extent=184)

    ##小兔的脚
    ##左脚
    t.pu()
    t.goto(-162, -260)  #
    t.pd()
    t.seth(0)
    t.circle(radius=41)
    # 右脚
    t.pu()
    t.goto(164, -260)
    t.pd()
    t.circle(radius=41)

    t.pu()  # 起笔
    t.goto(160, -139)  # 将画笔移动到指定位置
    t.pd()  # 落笔
    t.begin_fill()
    t.color('orange')
    t.circle(radius=30)  # radius半径属于circle函数、类型为float型
    t.end_fill()
    t.pu()


def star_draw(start_position, side):
    t.pu()
    t.goto(start_position)
    t.pd()
    t.color('yellow')
    t.begin_fill()
    t.forward(side)
    for i in range(1, 5):
        t.left(72)
        t.forward(side)
        t.right(144)
        t.forward(side)

    t.end_fill()
    t.seth(0)
    t.pu()


def draw_grass(x, y):
    t.pu()
    t.begin_fill()
    t.color('green')
    t.pensize(3)
    t.goto(x, y)
    t.pd()
    t.goto(x + 20, y + 50)
    t.goto(x + 30, y)
    t.goto(x + 40, y + 80)
    t.goto(x + 50, y + 30)
    t.goto(x + 60, y + 60)
    t.goto(x + 70, y)
    t.goto(x, y)
    t.end_fill()
    t.pu


pos = [(-200, 300), (-160, 279), (-130, 290), (-120, 260), (-90, 300), (-60, 283), (-30, 299), (0, 260),
       (30, 266),
       (50, 280), (70, 260), (90, 293), (120, 278), (-190, 270)]
size = [6, 3, 5, 6, 4, 3, 4, 5, 3, 5, 7, 3, 5, 6]
for item in range(0, len(size)):
    star_draw(pos[item], size[item])
draw_bat()
pos1 = [(-300, -300), (-200, -280), (-100, -320), (60, -299), (220, -330)]
for item in pos1:
    draw_grass(item[0], item[1])
t.done()
