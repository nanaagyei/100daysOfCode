from turtle import Turtle, Screen

# Set up game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("2D Snake Game")

# Create turtle (snake)
snake = Turtle('square')
snake.color("white")

screen.exitonclick()
