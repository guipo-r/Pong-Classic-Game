# Imports
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.color('red')
        self.goto(-100, 270)
        self.write("Player 1", align='center', font=('Courier', 12, 'normal'))
        self.color('white')
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.color('cyan')
        self.goto(100, 270)
        self.write("Player 2", align='center', font=('Courier', 12, 'normal'))
        self.color('white')
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def p1_wins(self):
        self.goto(0, 50)
        text = "Player 1 wins!"
        self.write(text, align='center', font=('Courier', 50, 'normal'))

    def p2_wins(self):
        self.goto(0, 50)
        text = "Player 2 wins!"
        self.write(text, align='center', font=('Courier', 50, 'normal'))
