from turtle import Turtle

class Score(Turtle):
    def __init__(self, paddle_l, paddle_r):
        super().__init__()
        self.goto(0,240)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(f"{paddle_l} - {paddle_r}", False, align="center", font=("Arial", 24, "bold"))
    
    def resetPoint(self, paddle_l, paddle_r):
        self.clear()
        self.write(f"{paddle_l} - {paddle_r}", False, align="center", font=("Arial", 24, "bold"))
