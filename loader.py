import turtle
from random import randint

def midpoint(pt1,pt2):
    # Find midpoint value between 2 numbers.
    return (pt1 + pt2) / 2


window = turtle.Screen()
window.bgcolor("white")
window_width, window_height = window.screensize()

# Create turtle and set up params
triangle = turtle.Turtle()
triangle.hideturtle()
triangle.speed(0)

# Set up 3 points of the triangle
pointAx = 0
pointAy = -window_height
pointBx = -window_width
pointBy = window_height
pointCx = window_width
pointCy = window_height

triangle.penup()
triangle.setposition(pointAx, pointAy)
triangle.pendown()
triangle.dot()
triangle.penup()
triangle.setposition(pointBx, pointBy)
triangle.pendown()
triangle.dot()
triangle.penup()
triangle.setposition(pointCx, pointCy)
triangle.pendown()
triangle.dot()

# Iterate
count = 10000
while count > 0:
    triangle.penup()
    new_X = ''
    new_Y = ''
    destination_point = randint(1,3)
    current_X, current_Y = triangle.position()
    if destination_point == 1:
        # Use point A
        new_X = (current_X + pointAx) / 2
        new_Y = (current_Y + pointAy) / 2
    if destination_point == 2:
        # Use point B
        new_X = (current_X + pointBx) / 2
        new_Y = (current_Y + pointBy) / 2

    if destination_point == 3:
        # Use point C
        new_X = (current_X + pointCx) / 2
        new_Y = (current_Y + pointCy) / 2
    triangle.setposition(new_X,new_Y)
    triangle.pendown()
    triangle.dot()
    count = count - 1

window.exitonclick()
