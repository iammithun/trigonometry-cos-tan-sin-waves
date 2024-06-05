import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Trigonometric Waves with Turtle Graphics")

# Create turtles for each wave
cosine_turtle = turtle.Turtle()
sine_turtle = turtle.Turtle()
tangent_turtle = turtle.Turtle()

# Set the speed of the turtles
cosine_turtle.speed(0)
sine_turtle.speed(0)
tangent_turtle.speed(0)

# Set the colors for each wave
cosine_turtle.color("blue")
sine_turtle.color("red")
tangent_turtle.color("green")

# Lift the pens to move without drawing
cosine_turtle.penup()
sine_turtle.penup()
tangent_turtle.penup()

# Move the turtles to the starting point
cosine_turtle.goto(-360, 100)  # Start position for cosine wave
sine_turtle.goto(-360, 0)      # Start position for sine wave
tangent_turtle.goto(-360, -100)# Start position for tangent wave

# Lower the pens to start drawing
cosine_turtle.pendown()
sine_turtle.pendown()
tangent_turtle.pendown()

# Draw the waves
for x in range(-360, 361):
    y_cos = 100 * math.cos(math.radians(x))
    y_sin = 100 * math.sin(math.radians(x))
    y_tan = 100 * math.tan(math.radians(x))
    
    # To handle large values of tangent, avoid drawing them
    if abs(y_tan) > 300:
        tangent_turtle.penup()
    else:
        tangent_turtle.pendown()
    
    cosine_turtle.goto(x, y_cos + 100)  # Adjusting y position for separation
    sine_turtle.goto(x, y_sin)
    tangent_turtle.goto(x, y_tan - 100) # Adjusting y position for separation

# Hide the turtles
cosine_turtle.hideturtle()
sine_turtle.hideturtle()
tangent_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
