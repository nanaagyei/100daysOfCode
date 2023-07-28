from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)
        self.color("white")

# Function paddle movements
    def up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)
