from turtle import Turtle
import turtle
from turtle import Screen
import time



def HeadText():
    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    turtle.setposition(-198, 227)
    turtle.write('Side 1', font=style, align='center')
    turtle.penup()
    turtle.setposition(-98, 227)
    turtle.write('Side 2', font=style, align='center')
    turtle.penup()
    turtle.setposition(2, 227)
    turtle.write('Side 3', font=style, align='center')
    turtle.penup()
    turtle.setposition(102, 227)
    turtle.write('Side 4', font=style, align='center')
    turtle.hideturtle()
    # time.sleep(5000);

def Base():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.penup()
        pen9.speed(100)
        pen9.sety(-100)
        pen9.setx(-200+(i*100))
        pen9.shapesize(1, 2)
        pen9.color('grey')

    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    turtle.setposition(-300,-157)
    turtle.write('Total Cars :', font=style, align='center')
    turtle.penup()
    turtle.setposition(-309, -177)
    turtle.write('Passing Cars :', font=style, align='center')
    turtle.penup()
    turtle.setposition(-277, -197)
    turtle.write('Time :', font=style, align='center')
    turtle.penup()
    turtle.hideturtle()
    # time.sleep(5000);

def Pole():
    for i in range(0, 4):
        pen9 = Turtle(shape='square')
        pen9.shapesize(9, 1)
        pen9.color('white')
        pen9.speed(100)
        pen9.penup()
        pen9.sety(-15)
        pen9.setx(-200+(i*100))
        pen9.color('grey')
        # time.sleep(5000);


def Back():
    for i in range(0,4):
        pen9 = Turtle(shape='square')
        pen9.color('white')
        pen9.shapesize(7.6, 2.5)
        pen9.speed(100)
        pen9.color('grey')
        pen9.penup()
        pen9.sety(150)
        pen9.setx(-200+(i*100))
        # time.sleep(5000);

def Red(Num):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('red')
    pen1.penup()
    pen1.sety(200)
    pen1.setx(-200 + (i * 100))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(150)
    pen2.setx(-200 + (i * 100))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + (i * 100))
    # time.sleep(5000);

def Yellow(Num):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(200)
    pen1.setx(-200 + (i * 100))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('yellow')
    pen2.penup()
    pen2.sety(150)
    pen2.setx(-200 + (i * 100))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(2)
    pen3.color('white')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + (i * 100))
    # time.sleep(5000);

def Green(Num,TCars,PCars,Time):
    i=Num-1
    pen1 = Turtle(shape='circle')
    pen1.color('white')
    pen1.speed(100)
    pen1.shapesize(2)
    pen1.color('white')
    pen1.penup()
    pen1.sety(200)
    pen1.setx(-200 + ((i) * 100))

    pen2 = Turtle(shape='circle')
    pen2.color('white')
    pen2.speed(100)
    pen2.shapesize(2)
    pen2.color('white')
    pen2.penup()
    pen2.sety(150)
    pen2.setx(-200 + ((i) * 100))

    pen3 = Turtle(shape='circle')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(2)
    pen3.color('green')
    pen3.penup()
    pen3.sety(100)
    pen3.setx(-200 + ((i) * 100))

    turtle.color('black')
    style = ('Courier', 14,)
    turtle.speed(1000)
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-147)
    pen3.setx(-200 + ((i) * 100))
    turtle.setposition(-200+(i*100), -157)
    turtle.write(TCars,font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-167)
    pen3.setx(-200 + ((i) * 100))
    turtle.setposition(-200+(i*100), -177)
    turtle.write(PCars, font=style, align='center')
    turtle.penup()
    pen3 = Turtle(shape='square')
    pen3.color('white')
    pen3.speed(100)
    pen3.shapesize(1)
    pen3.color('white')
    pen3.penup()
    pen3.sety(-187)
    pen3.setx(-200 + ((i) * 100))
    turtle.setposition(-200+(i*100), -197)
    turtle.write(Time, font=style, align='center')
    turtle.hideturtle()
    # time.sleep(5000);

def Reset():
    Yellow(1)
    Yellow(2)
    Yellow(3)
    Yellow(4)
    # time.sleep(5000);

# HeadText()