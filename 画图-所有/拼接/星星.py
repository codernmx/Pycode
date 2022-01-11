import turtle
import random

def star():
    for i in range(5):
        turtle.fd(15)
        turtle.right(144)

def go():
    turtle.penup()
    turtle.goto(random.randint(-350, 350), random.randint(-350, 350))
    turtle.pendown()

def colour():
    turtle.pencolor("gold")

def main():
    turtle.width(5)
    a = 20
    turtle.speed(0)
    turtle.bgcolor('black')
    for w in range(20):
        star()
        go()
        colour()
    turtle.done()

if __name__ == '__main__':
    main()
