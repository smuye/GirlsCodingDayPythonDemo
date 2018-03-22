# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import turtle
t1=turtle.Turtle()
#长方形
t1.fd(100)
t1.left(90)
t1.fd(150)
t1.left(90)
t1.fd(200)
t1.left(90)
t1.fd(150)
t1.left(90)
t1.fd(100)

#三角形
t1.penup()
t1.goto(-120,150)
t1.pendown()


t1.fd(240)
t1.left(135)
t1.fd(170)
t1.left(90)
t1.fd(170)

#弧形
t1.penup()
t1.goto(0,270)
t1.pendown()

t1.forward(40)
t1.left(90)
t1.circle(40,90)

t1.penup()
t1.goto(0,270)
t1.pendown()

t1.right(180)
t1.forward(60)
t1.left(90)
t1.circle(60,90)

t1.penup()
t1.goto(0,0)
t1.pendown()
t1.home()
#door
t1.penup()
t1.goto(30,0)
t1.pendown()

t1.left(90)
t1.fd(80)
t1.right(90)
t1.fd(40)
t1.right(90)
t1.fd(80)
#windows
t1.penup()
t1.goto(-10,130)
t1.pendown()

t1.fd(60)
t1.rt(90)
t1.fd(60)
t1.rt(90)
t1.fd(60)
t1.rt(90)
t1.fd(60)
t1.rt(90)
t1.fd(30)
t1.rt(90)
t1.fd(60)
t1.rt(90)
t1.fd(30)
t1.rt(90)
t1.fd(30)
t1.rt(90)
t1.fd(60)

#烟囱
t1.penup()
t1.goto(0,270)
t1.pendown()

t1.lt(45)
t1.fd(50)
t1.lt(135)
t1.fd(30)
t1.rt(90)
t1.fd(20)
t1.rt(90)
t1.fd(50)



turtle.done()
