# import colorgram
#
# colors = colorgram.extract('image.jpg', 50)
#
# extracted_colors = []
#
# for n in range(len(colors)):
#     color_1 = colors[n]
#     extracted_colors.append((color_1.rgb[0],color_1.rgb[1], color_1.rgb[2]))
#
# print(extracted_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(0)
tim.hideturtle()
tim.pu()
tim.setpos(-100, -100)

color_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
              (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
              (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
              (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244),
              (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105), (91, 153, 156), (45, 49, 45), (104, 52, 26),
              (161, 202, 213), (213, 203, 31)]


def horizontal():
    for _ in range(10):
        tim.dot(15, random.choice(color_list))
        tim.pu()  # penup
        tim.fd(30)


y = -100


for _ in range(10):
    horizontal()
    y += 25
    tim.setpos(-100, y)


my_screen = Screen()
my_screen.exitonclick()
