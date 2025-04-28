import time
from turtle import Screen
from paddle import *
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")


left_paddle = Paddle(LEFT_PADDLE_START_POS)
right_paddle = Paddle(RIGHT_PADDLE_START_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_increase()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_increase()


screen.exitonclick()