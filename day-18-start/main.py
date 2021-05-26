from turtle import Turtle, Screen
import random

tim = Turtle()


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.color(r, g, b)


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(50)
#         tim.right(angle)
#         # tim.forward(50)


# timmy_the_turtle.shape('turtle')
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()

# for n in range(3, 9):
#     change_color()
#     draw_shape(n)

# angle = [0, 90, 180, 270]
# tim.pensize(10)
tim.speed(0)

# for _ in range(100):
#     change_color()
#     tim.fd(20)
#     tim.right(random.choice(angle))

for _ in range(72):
    change_color()
    tim.circle(100)
    tim.left(5)

screen = Screen()
screen.exitonclick()
