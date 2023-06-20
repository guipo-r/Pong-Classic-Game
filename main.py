# Imports
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)  # I want to skip the first goto() animation

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create ball
ball = Ball()

# Create scoreboard
score_board = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Remember not to write () after go_up function for this to work
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Add a little delay so the ball moves slower
    screen.update()  # Update screen after first goto() animation
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.xcor() == 330 or ball.xcor() == -330:  # In order to also count extremes of paddle
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.hit_pad()

    # Detect a goal
    if ball.xcor() > 380:
        score_board.l_point()
    elif ball.xcor() < -380:
        score_board.r_point()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()

    # Check scores
    if score_board.l_score == 3:
        score_board.p1_wins()
        game_is_on = False
    elif score_board.r_score == 3:
        score_board.p2_wins()
        game_is_on = False

screen.exitonclick()
