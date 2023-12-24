import turtle

# Screen setup
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
brick_rows = 4
brick_columns = 8
brick_gap = 5
brick_width = 80
brick_height = 20
bricks = []
bricks_colors = ["violet", "yellow", "red", "blue"]

for y in range(brick_rows):
    for x in range(brick_columns):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(bricks_colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick_x = -350 + (x * (brick_width + brick_gap))
        brick_y = 250 - (y * (brick_height + brick_gap))
        brick.goto(brick_x, brick_y)
        bricks.append(brick)

# Score
score = 0
lives = 3

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))


# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
        paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
        paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")


# Function to increase ball speed
def increase_speed():
    ball.dx *= 1.1
    ball.dy *= 1.1


# Main game loop
while True:
    win.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        lives -= 1
        score_display.clear()
        score_display.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    # Paddle collision
    if paddle.ycor() - 10 < ball.ycor() < paddle.ycor() + 10 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.isvisible() and brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10 and brick.xcor() - 40 < ball.xcor() < brick.xcor() + 40:
            ball.dy *= -1
            brick.hideturtle()
            score += 1
            increase_speed()
            score_display.clear()
            score_display.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    # Game over
    if lives == 0:
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))
        break
