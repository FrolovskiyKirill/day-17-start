import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    return r, g, b


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))




