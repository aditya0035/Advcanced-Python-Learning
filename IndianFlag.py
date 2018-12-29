from turtle import Turtle,Screen
import time
turtle=None
window=None
def Main():
    global turtle
    global window
    turtle = Turtle()
    turtle.hideturtle()
    window = Screen()
    window.setup(1.0,1.0,None,None)
    window.title("Indian flag")
    time.sleep(10)
    DrawIndianFlag(500, (150, 150))
    HoldWinodow()

def HoldWinodow():
    window.exitonclick()

#turtle.setheading(90) #we can use turtle.left(90)
#turtle.goto(0,-200) #it will set the co-ordinate if turtle to(0,-200)
"""but here we have to hide the line so """
def DrawPole(length):
    turtle.up()
    turtle.goto(0,-200)
    turtle.down()
    turtle.setheading(90)
    turtle.forward(length)

def DrawSquare(l,w,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(l)
    turtle.end_fill()


def DrawSpoke(count,centerposition,radius):
    arcangle=360/count
    turtle.up()
    turtle.goto(centerposition)
    turtle.down()
    for i in range(count):
        turtle.forward(radius)
        turtle.up()
        turtle.goto(centerposition)
        turtle.down()
        turtle.right(arcangle)

def ReachToCentreOfAshokaChakra(length,windth):
    oneblockWidth=windth/3
    turtle.up()
    turtle.right(90)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.forward(oneblockWidth+(oneblockWidth/2))
    turtle.setheading(90)
    turtle.down()
def DrwaAshokaChakra(redius,centerposition):
    x,y=centerposition
    x+=redius
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(radius=redius)

def DrawIndianFlag(poleLength,flagDimeshion):
    length,windth=flagDimeshion
    oneSquareLength=length/3
    DrawPole(poleLength)
    DrawSquare(3*oneSquareLength, windth, "green")
    DrawSquare(2*oneSquareLength, windth, "white")
    DrawSquare(oneSquareLength, windth, "orange")
    ReachToCentreOfAshokaChakra(length,windth)
    centrePosition= turtle.pos()
    radius=windth/6
    DrwaAshokaChakra(radius,centrePosition)
    DrawSpoke(26,centrePosition,radius)

Main()
