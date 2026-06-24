from turtle import Turtle, Screen, colormode
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

screen = Screen()
jimmy = Turtle()
colormode(255)
jimmy.speed('fastest')
jimmy.hideturtle()

color_list = [(150, 70, 97), (54, 99, 154), (134, 179, 204), (231, 136, 62),
             (200, 147, 177), (113, 82, 60), (199, 78, 109), (144, 134, 73), (143, 191, 142), (227, 92, 62),
             (74, 101, 90), (226, 160, 183), (69, 161, 90), (5, 165, 176), (116, 126, 140), (173, 192, 213),
             (159, 201, 220), (22, 65, 114), (241, 171, 157), (173, 203, 182), (17, 58, 99), (171, 32, 37),
             (174, 31, 29)]

for i in range(5):
    for j in range(7):
        color = color_list[random.randint(0, len(color_list) - 1)]
        jimmy.teleport(-180 + j * 40, -180 + i * 40)
        jimmy.dot(20, color)

screen.exitonclick()