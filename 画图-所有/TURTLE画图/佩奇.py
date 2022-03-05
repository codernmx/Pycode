# @Time : 2021/12/12 20:17
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
from turtle import *
def nose(x,y):#鼻子
    penup()#提起笔
    goto(x,y)#定位
    pendown()#落笔，开始画
    setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    begin_fill()#准备开始填充图形
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            left(3) #向左转3度
            forward(a) #向前走a的步长
        else:
            a=a-0.08
            left(3)
            forward(a)
    end_fill()#填充完成

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)#画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)#返回或设置pencolor和fillcolor
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()


def head(x,y):#头
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y): #耳朵
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()


def eyes(x,y):#眼睛
    color((255,155,192),"white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255,155,192),"white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):#腮
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y): #嘴
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)

def body(x,y):#身体
    color("red",(255,99,71))
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(-130)
    circle(100,10)
    circle(300,30)
    setheading(0)
    forward(230)
    setheading(90)
    circle(300,30)
    circle(100,3)
    color((255,155,192),(255,100,100))
    setheading(-135)
    circle(-80,63)
    circle(-150,24)
    end_fill()


def hands(x,y):#手
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(-160)
    circle(300,15)
    penup()
    setheading(90)
    forward(15)
    setheading(0)
    forward(0)
    pendown()
    setheading(-10)
    circle(-20,90)

    penup()
    setheading(90)
    forward(30)
    setheading(0)
    forward(237)
    pendown()
    setheading(-20)
    circle(-300,15)
    penup()
    setheading(90)
    forward(20)
    setheading(0)
    forward(0)
    pendown()
    setheading(-170)
    circle(20,90)

def foot(x,y):#脚
    pensize(10)
    color((240,128,128))
    penup()
    goto(x,y)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)

    pensize(10)
    color((240,128,128))
    penup()
    setheading(90)
    forward(40)
    setheading(0)
    forward(90)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)

def tail(x,y):#尾巴
    pensize(4)
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    seth(0)
    circle(70,20)
    circle(10,330)
    circle(70,30)

def setting():          #参数设置
    pensize(4)
    hideturtle()        #使乌龟无形（隐藏）
    colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255,155,192),"pink")
    setup(840,500)
    speed(10)

def main():
    setting()           #画布、画笔设置
    nose(-100,100)      #鼻子
    head(-69,167)       #头
    ears(0,160)         #耳朵
    eyes(0,140)         #眼睛
    cheek(80,10)        #腮
    mouth(-20,30)       #嘴
    body(-32,-8)        #身体
    hands(-56,-45)      #手
    foot(2,-177)        #脚
    tail(148,-155)      #尾巴
    done()

if __name__ == '__main__':
    main()