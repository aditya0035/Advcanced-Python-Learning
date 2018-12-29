"""
We can control the turtle speed as well using
"""
from turtle import *

turtle=Turtle()
turtle.speed(1)
print(help(turtle.speed))

"""
we can fill color into our created shape using
turtle_beginfill
turtle.fillcolor("color name")
turtle_endfill
"""

turtle.fillcolor("light green")
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

window=Screen()
window.exitonclick()
