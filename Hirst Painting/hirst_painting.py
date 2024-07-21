from turtle import Turtle, Screen
import random

colors = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85),
          (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177),
          (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111),
          (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85),
          (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201),
          (213, 182, 176), (37, 47, 45)]


def create_row(t):
    for i in range(10):
        t.dot(20, random.choice(colors))
        t.fd(50)


def reposition(t, y, counter):
    t.teleport(-300, (y + (counter * 50)))


def main():
    t = Turtle()
    screen = Screen()
    t.penup()
    t.speed(0)
    t.hideturtle()
    screen.colormode(255)
    y = -250
    counter = 0

    while counter != 10:
        reposition(t, y, counter)
        create_row(t)
        counter += 1

    screen.exitonclick()


if __name__ == '__main__':
    main()

    
# The code below was used to extract the rgb values from painting.jpg
# import colorgram
# colors = colorgram.extract('painting.jpg', 30)
# color_list = []
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)
