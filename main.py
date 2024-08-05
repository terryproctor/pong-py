from paddle import Paddle
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=850, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

screen.exitonclick()