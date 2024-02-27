from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

def point():
    ball.goto(0,0)
    ball.bounce_x()
    score.resetPoint(paddle_l.score, paddle_r.score)
    screen.update()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create a paddle
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

# Movement of the paddles
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

# Create a ball
ball = Ball()

# Create a score
score = Score(paddle_l.score, paddle_r.score)

game_is_on = True
screen.update()
time.sleep(1)
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        paddle_l.point()
        point()
        time.sleep(1)
    elif ball.xcor() < -380:
        paddle_r.point()
        point()
        time.sleep(1)
    if paddle_r.score == 5 or paddle_l.score == 5:
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        score.goto(0,0)
        score.write("Game Over", False, align="center", font=("Arial", 24, "bold"))
        score.goto(0,-34)
        score.write(f"{paddle_l.score} - {paddle_r.score}", False, align="center", font=("Arial", 24, "bold"))


screen.exitonclick()