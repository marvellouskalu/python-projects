import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create a list of colors for turtles
colors = ["red", "blue", "green", "orange", "purple", "yellow"]

# Create a list to store the turtles
turtles = []

# Create turtles and add them to the list
for i in range(6):
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(-350, 200 - i * 80)  # Position the turtles on the starting line
    turtles.append(turtle_obj)

# Create a finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(350, 250)
finish_line.pendown()
finish_line.goto(350, -250)
finish_line.penup()


# Function to move the turtles forward randomly
def move_turtles():
    for turtle_obj in turtles:
        distance = random.randint(1, 20)
        turtle_obj.forward(distance)


# Function to check if any turtle has reached the finish line
def check_winner():
    for turtle_obj in turtles:
        if turtle_obj.xcor() >= 350:
            return True
    return False


# Main game loop
while True:
    move_turtles()
    if check_winner():
        break

# Find the winning turtle(s)
winners = []
for turtle_obj in turtles:
    if turtle_obj.xcor() >= 350:
        winners.append(turtle_obj.color())

# Display the winner(s)
if len(winners) == 1:
    print("The winner is the turtle with color:", winners[0])
else:
    print("It's a tie between turtles with colors:", winners)

# Keep the window open until it is closed manually
turtle.done()
