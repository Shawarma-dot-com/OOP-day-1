import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("circle")
screen = Screen()
tim.shapesize(0.5)
# for creating a dotted line
'''for _ in range(4):
    tim.forward(100)
    tim.left(90)'''
# for creating a square
'''for _ in range(20):
    tim.forward(5)
    tim.up()
    tim.forward(5)
    tim.down()'''
# for creating shapes that start with 3 sides and end with 10
'''colour_picker = ["royal blue", "light green", "dark orange", "pink", "maroon", "dark slate blue"]
colour_random = random.choice(colour_picker)
colour_random2 = random.choice(colour_picker)


def no_rep_colour():
    a = tim.color(colour_random)
    if a == a:
        return tim.color(random.choice(colour_picker))


sides = 2


on = True
while on:

    no_rep_colour()

    sides += 1
    angle = 360/sides

    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)

    if sides == 10:
        on = False'''


# for crating random walk


'''colour_picker = ["royal blue", "light green", "dark orange", "pink", "dark orange", "aquamarine", "salmon",
                 "dodger blue", "gold"]
screen.colormode(225)
direction = [0, 90, 180, 270]


turtle.colormode(2)

def random_color():

    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    random_colour = (r, g, b)
    return random_colour


tim.speed("fastest")
tim.pensize(20)
global tup
for _ in range(1000):

    tim.color(random.choice(colour_picker))
    tim.forward(30)
    tim.setheading(random.choice(direction))'''

# For drawing a circle pattern
'''tim.speed("fastest")
colour_picker = ["royal blue", "light green", "dark orange", "pink", "dark orange", "aquamarine", "salmon",
                 "dodger blue", "gold"]


def density_of_circle(density_number):

    for _ in range(int(360 / density_number)):
        tim.color("pink")
        tim.circle(100)
        tim.setheading(tim.heading()+density_number)


density_of_circle(10.0)'''
