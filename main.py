from paddle import Paddle
from ball import Ball
from turtle import Screen
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)

game_ball = Ball()

game_scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    # Detect collision with paddles
    if game_ball.distance(right_paddle) < 40 and game_ball.xcor() > 330 or game_ball.distance(left_paddle) < 40 and game_ball.xcor() < -330:
        game_ball.bounce_x()

    # Detect when ball goes out of bounds
    if game_ball.xcor() > 380:
        game_scoreboard.l_score += 1
        game_scoreboard.update_scoreboard()
        game_ball.reset_position()
    if game_ball.xcor() < -380:
        game_scoreboard.r_score += 1
        game_scoreboard.update_scoreboard()
        game_ball.reset_position()
        


    
    sleep(0.05)
    screen.update()

screen.exitonclick()