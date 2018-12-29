"""
In this module we will draw circle
"""
from turtle import *

turtle=Turtle()
turtle.circle(100) #it will draw a circle of 100 radius

turtle.reset() #it will reset the turtle
turtle.circle(100,180) #will draw a circle of 100 radius and extent is 180 degree that is a semi circle

turtle.undo() #it will undo the turtle last action
turtle.circle(100,steps=3) #it will draw a triangle
turtle.reset()
turtle.circle(100,steps=4) #it will draw a square
turtle.reset()

turtle.circle(100,180,3)
turtle.reset()
window=Screen()
window.exitonclick()
