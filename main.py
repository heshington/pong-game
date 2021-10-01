from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.setup(width=800, height=600)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

#event listners

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")



game_on = True
while game_on:

    screen.update()




screen.exitonclick()