from turtle import Turtle

RIGHT_PADDLE_START_POS = (350, 0)
LEFT_PADDLE_START_POS = (-350, 0)


class Paddle(Turtle):
    def __init__(self, paddle_start_pos):
        """direction means "left" or "right" """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setposition(paddle_start_pos)
        self.left(90)
        self.turtlesize(1, 5)

    def paddle_up(self):
        self.forward(40)
    def paddle_down(self):
        self.back(40)