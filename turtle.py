import turtle


# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the turtle's speed to the maximum
pen.width(2)  # Set the width of the pen

# Draw a colorful pattern
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]

for angle in range(360):
    pen.color(colors[angle % len(colors)])
    pen.forward(angle)
    pen.right(59)  # Angle to create a spiral effect

# Close the turtle graphics window on click
screen.exitonclick()

