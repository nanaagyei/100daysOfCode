import turtle

sketch = turtle.Turtle()
screen = turtle.Screen()
screen.title("Etch a Sketch")


def move_forward():
    sketch.forward(10)


def move_backward():
    sketch.backward(10)


def counter_clockwise():
    new_heading = sketch.heading() - 10
    sketch.setheading(new_heading)


def clockwise():
    new_heading = sketch.heading() + 10
    sketch.setheading(new_heading)


def clear_screen():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
