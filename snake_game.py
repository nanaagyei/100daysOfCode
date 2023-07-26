import turtle  # Imports the turtle lib
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Setting up the screen
wn = turtle.Screen()  # Screen display
wn.title("Snake Game by N_k@y")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

segments = []

# Pen(Score board)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.goto(0,260)
pen.hideturtle() # hides the turtle
pen.color("White")
pen.write("Score: 0   High Score: 0", align = "center", font=("Courier", 24, "normal"))

# Creating the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()  # doesn't draw any lines when it moves
head.goto(0,0)  # in the middle of the screen
head.direction = "stop"  # turtle doesn't move in any direction

# Snake food
food = turtle.Turtle()  # another turtle for the food
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


# Functions for to check for movements
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)


def go_up():
	if head.direction != "down":
		head.direction = "up"


def go_down():
	if head.direction != "up":
		head.direction = "down"


def go_left():
	if head.direction != "right":
		head.direction = "left"


def go_right():
	if head.direction != "left":
		head.direction = "right"


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop

while True:
	wn.update()  # updates the screen about any movement or changes

	# Check for border collision
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"

		# Hide the segments after collision
		for segment in segments:
			segment.goto(1000, 1000)

		# Clear the list
		segments.clear()

		# Reset delay
		delay = 0.1

		# Reset the score
		score = 0

		pen.clear()
		pen.write("Score: {}   High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

	# Check for collision with food
	if head.distance(food) < 20:
		# Move food to random spot
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x,y)

		# Add a new segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		# shorten the delay
		delay -= 0.001

		# Increase the score
		score += 5

		if score > high_score:
			high_score = score

		pen.clear() # clears the previous score board (or updates the score board)
		pen.write("Score: {}   High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

	# Move end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	# Move segment 0 to where head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()

	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"

			for segment in segments:
				segment.goto(1000, 1000)

			# Clear the list
			segments.clear()

			# Reset the score
			score = 0

			pen.clear()
			pen.write("Score: {}   High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

	time.sleep(delay)


turtle.done()
