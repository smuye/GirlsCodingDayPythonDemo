# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import turtle
t1=turtle.Turtle()


#六角彩
def draw():
    t1.forward(15)
    t1.right(60)
    t1.fd(30)
    t1.left(60)
    t1.fd(30)
    return

color=['gray','blue','green','yellow','red','purple']
for i in range(6):   
    t1.pencolor(color[i])
    t1.left(90)
    draw()
    t1.right(150)

turtle.done()



#填充三个半圆
def semi():
  t1.color('blue','yellow')
  t1.begin_fill()
  t1.forward(100)
  t1.left(90)
  t1.circle(50,180)
  t1.left(90)
  t1.end_fill()
  return

t1.left(60)
semi()
t1.forward(100)
t1.right(120)
semi()
t1.forward(100)
t1.right(120)
semi()

turtle.done()

