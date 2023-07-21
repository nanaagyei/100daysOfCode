import turtle
import random

# tim = Turtle()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

shape = turtle.Turtle()
colorList = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen',
             'wheat', 'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]
turtle.colormode(255)
shape.speed('fast')


# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         shape.forward(100)
#         shape.right(angle)
#
#
# for shape_side in range(3, 11):
#     shape.color(random.choice(colorList))
#     draw_shape(shape_side)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        shape.color(random_color())
        shape.circle(100)
        shape.setheading(shape.heading() + size_of_gap)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
