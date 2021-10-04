from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.setup(width=800, height=600)

# Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Ball
ball = Ball()
# scoreboard
scoreboard = Scoreboard()

# event listners

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with either paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if the ball goes out of bounds left player scores
    if ball.xcor() > 380:
        ball.reset()
        ball.x_move = -10
        scoreboard.l_point()
    # # detect if ball goes out of bounds right player scores
    if ball.xcor() < -380:
        ball.reset()
        ball.x_move = 10
        scoreboard.r_point()

screen.exitonclick()
