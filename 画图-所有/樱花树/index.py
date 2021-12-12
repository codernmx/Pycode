import turtle as t
import time, random



# 画樱花的躯干
# 画樱花的躯干
def Tree(branch, t):
  time.sleep(0.0005)
  if branch > 3:
    if 8 <= branch <= 12:
      if random.randint(0, 2) == 0:
        # 白色
        t.color('snow')
      else:
        # 淡珊瑚色
        t.color('lightcoral')
      t.pensize(branch / 3)
    elif branch < 8:
      if random.randint(0, 1) == 0:
        t.color('snow')
      else:
        t.color('lightcoral')
      t.pensize(branch / 2)
    else:
      # 赭色
      t.color('sienna')
      t.pensize(branch / 10)
    t.forward(branch)
    a = 1.5 * random.random()
    t.right(20 * a)
    b = 1.5 * random.random()
    Tree(branch - 10 * b, t)
    t.left(40 * a)
    Tree(branch - 10 * b, t)
    t.right(20 * a)
    t.up()
    t.backward(branch)
    t.down()
# 掉落的花瓣
def Petal(m, t):
  for i in range(m):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.down()
    t.color('lightcoral')
    t.circle(1)
    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)
#改变颜色
def changeColor():
    t.up()
    t.color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.goto(330, 200)
    t.write('青海民族大学', font=("Arial", 18, "normal"))
    t.goto(350, 170)
    t.write('热烈庆祝中国共产党', font=("Arial", 18, "normal"))
    t.goto(370, 140)
    t.write('成立100周年', font=("Arial", 18, "normal"))


# 绘图区域

# 隐藏画笔
t.hideturtle()
t.getscreen().tracer(5, 0)
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干

t.hideturtle()  # 影藏最终箭头

#画星星
def pentagram(size, x, y, seth=0):
    t.goto(x, y)
    t.setheading(seth)
    t.backward(size * 1.1756 / 2)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()
def drawflag():
    t.penup()
    t.goto(360, -10)
    t.pendown()
    color = 'red'
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(100)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()
    t.penup()
    t.pencolor('yellow')
    t.fillcolor('yellow')
    pentagram(51, 390, 50)
    pentagram(20, 440, 80, 30)
    pentagram(20, 460, 60, -30)
    pentagram(20, 460, 30)
    pentagram(20, 450, 10, 30)
    t.pendown()

#
Tree(60, t) #樱花树
# 掉落的花瓣
Petal(200, t)
# drawflag() #旗子


t.penup()
t.goto(360, 90)
t.pensize(1)
t.pendown()
t.goto(360, -100)

# while True:
#     time.sleep(1)
#     changeColor() #改变颜色

t.done()  #不闪退


