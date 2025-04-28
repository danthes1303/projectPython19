import random
from random import choice
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1.10
    def bounce_x(self):
        self.x_move *= -1.10

    def refresh(self):
        self.setposition(0,0)
        self.bounce_x()
        self.y_move = 10
        self.x_move = 10
        r = random.randint(1,2)
        if r == 1:
            self.bounce_y()
        else:
            pass

