#import os
#import random

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

    def move(self):
        self.fd(self.speed)

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -=1



#Create my Sprites 
player = Player("triangle", "white", 0, 0)

#Keyboard binding 
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.turn_accelerate, "Up")
turtle.onkey(player.turn_decelerate, "Down")
turtle.listen()

# Main Game loop 
while True: 
    player.move()



#delay = raw_input("Please enter to finish. >")