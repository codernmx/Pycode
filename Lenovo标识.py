import turtle as t
t.penup()
t.speed(20)
t.hideturtle()  # 影藏最终箭头
t.screensize(500,250, "red")
t.setup(500,250,700,300)
t.goto(0, -40)
t.color('black')
t.width(15)
t.write('Lenovo',move=True, font=("Arial", 64, "normal"), align='center')
t.goto(150, 25)
t.write('TM',move=True, font=("Arial", 20, "normal"), align='center')
t.done()
