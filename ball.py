from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)   

    def bounce_y(self):
        self.ymove = -1 * self.ymove 

    def bounce_x(self):
        self.xmove = -1 * self.xmove

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
