from turtle import Turtle, Screen
import random


screen= Screen()
screen.setup(width= 800, height= 600)
screen.bgpic('road.gif')


y_positions= [-260,-172, - 85, 2, 85, 172, 260]
colors= ["green", "red", "white", "yellow", "purple", "blue"]
all_turtle= []

for index in range(0, 7):
    new_tur= Turtle(shape= 'turtle')
    new_tur.shapesize(2)
    new_tur.penup()
    new_tur.goto(x= -350, y= y_positions[index])
    new_tur.color(colors[index])
    all_turtle.append(new_tur)

is_on = True

while is_on:
    for turtle in all_turtle:
        random_pace = random.randint(0, 7)
        turtle.forward(random_pace)

screen.exitonclick()
