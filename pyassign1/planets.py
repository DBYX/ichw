# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:11:29 2017

@author: 惠普
"""

import turtle


import math


Mercury = turtle.Turtle() 
Mercury.color("blue")

Venus=turtle.Turtle()
Venus.color("yellow")

Earth=turtle.Turtle()
Earth.color("black")

Mars=turtle.Turtle()
Mars.color("red")

Jupiter=turtle.Turtle()
Jupiter.color("purple")

Saturn=turtle.Turtle()
Saturn.color("orange")

Mercury.penup()
Mercury.goto(50,0)
Mercury.pendown()
Mercury.speed(0)

Venus.penup()
Venus.goto(75,0)
Venus.pendown()
Venus.speed(0)

Earth.penup()
Earth.goto(100,0)
Earth.pendown()
Earth.speed(0)

Mars.penup()
Mars.goto(125,0)
Mars.pendown()
Mars.speed(0)

Jupiter.penup()
Jupiter.goto(150,0)
Jupiter.pendown()
Jupiter.speed(0)

Saturn.penup()
Saturn.goto(175,0)
Saturn.pendown()
Saturn.speed(0)

degree=0    

while 1>0:
    a=50
    b=35
    for planet in [Mercury,Venus,Earth,Mars,Jupiter,Saturn]:
        planet.goto(a*math.cos(degree),b*math.sin(degree))
        a=a+25
        b=b+22
    degree=degree+math.pi/100
        


    