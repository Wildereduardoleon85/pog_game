from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()


game_is_on = True


screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    collided_with_right_paddel = ball.distance(r_paddle) < 50 and ball.xcor() >= 360
    collided_with_left_paddel = ball.distance(l_paddle) < 50 and ball.xcor() <= -370

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collission with right paddle
    if collided_with_right_paddel or collided_with_left_paddel:
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() >= 380:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() <= -390:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
