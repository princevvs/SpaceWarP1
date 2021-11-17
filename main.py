import os
import random

#Important Turtle Module 
import turtle
#Shows the box
turtle.fd(0)
#Set the animation speed
turtle.speed(0)
#Set the background colour 
turtle.bgcolor("black")
#Hides default turtle 
turtle.ht()
#Saves memory 
turtle.setundobuffer(1)
#Speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1


#Create my Sprites 
player = Sprite("triangle", "white", 0, 0)






delay = raw_input("Please enter to finish. >")