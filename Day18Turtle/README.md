# Turtle Art - Hirst Dot Painting

This is a Python program that uses the Turtle graphics library to create a Hirst Dot Painting. The Hirst Dot Painting style was inspired by artist Damien Hirst's series of paintings consisting of rows of randomly colored dots.

## How It Works

The program sets up the Turtle graphics environment, including setting the color mode to RGB (0-255) and creating a Turtle object named `hirst`.

A list named `color_list` is defined, containing various RGB color tuples representing different colors used for the dots.

The Turtle `hirst` is configured with speed "fastest" to draw quickly and `hideturtle()` to hide the turtle icon.

The `hirst` turtle is positioned to start drawing at the bottom-left corner of the canvas.

The function `create_dot_line()` is defined to draw a row of 10 dots with random colors from the `color_list`.

The function `starting_point()` is defined to reposition the turtle at the start of the next row.

The main loop runs 10 times, each time calling `create_dot_line()` to draw a row of dots and then repositioning the turtle using `starting_point()` to start drawing the next row.

Finally, the program sets up the screen and waits for the user to click the window to exit the drawing.

## How to Run

Make sure you have Python and the Turtle graphics library installed on your system.

Copy the entire code into a Python file (e.g., `hirst_dot_painting.py`).

Run the Python script, and a new window with the drawing will appear.

Click inside the drawing window to close the program.

## Note

Feel free to modify the `color_list` or adjust the number of dots in a row to experiment with different patterns and styles for the Hirst Dot Painting. Have fun exploring the world of Turtle graphics!
