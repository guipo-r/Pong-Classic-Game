# Imports
from turtle import Turtle


# Create paddle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 260:  # After testing different values, this is the proper upper limit
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:  # After testing different values, this is the proper lower limit
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
