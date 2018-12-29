"""
Turtle is a simple & enjoyable way to draw pictures on screen
it also refers to controlling graphical entity in a graphics window with x,y co-ordinate
to work with turtle we need to import Turtle class from turtle module
"""
import turtle
aditya=turtle.Turtle() #will create a turtle with graphic window
#print(aditya.shape())
#print(help(aditya.shape)) # will show help for different shape avaliable
aditya.shape('turtle')
"""
We can change the color of turtle default color is in classic mode but we can change it ot 255 mode RGB
"""
aditya.color("Blue") #it will change the color of turtle
aditya.color("Blue","Red") #here it will change the color of turtle as well as  pen color used by turtle for drawing
"""above color of turtle will be red and color of pen will be blue"""

aditya.forward(100) #here distance is in pixel it will move turtle to that no of px
aditya.backward(200) #here it will move turtle that no of px in backward direction

aditya.forward(-100) #it will move turtle that no of px in backward direction as turtle work on x,y co-ordiates
aditya.backward(-400)

aditya.left(180) #it will set the turtle by 180 from current heading direction
aditya.right(160) #it will set turtle by that no of degree from cureent heading direction

aditya.setheading(200) #it will set the direction from +x asis

aditya.hideturtle() #this will hide the turtle


"""
co-ordinate of turtle is (0,0) which is called home position or origin
"""

wn=turtle.Screen() #allow us to access the turtle Graphihc window
wn.exitonclick()  #hold the turtle window till it is closes using close button
wn.bgcolor("red") #it will allow us to change background color we can change color mode to 255 to give bg color in RGB  format
#wn.bgpic() using this method we can provide the pic but it should be in same folder as current module is
