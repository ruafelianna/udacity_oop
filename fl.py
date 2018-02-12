import turtle
from math import pi, sqrt

def draw_flower(t, R, colors):
    p = round(sqrt(3) * R / 2)
    q = round(R / 2)
    coord = [(0,-2*R), (p,-3*q), (p,-q), (0,0), (-p,-q), (-p,-3*q), (0,-R)]
    for i in range(len(coord)):
        x,y = coord[i]
        t.up()
        t.goto(x, y)
        t.down()
        t.color(colors[i])
        t.circle(R)

COLORS = ["white", "white", "white", "white", "white", "white", "yellow"]
R = 50

if __name__ == "__main__":
    scr = turtle.Screen()
    scr.bgcolor("navy")

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)

    draw_flower(t, R, COLORS)

    scr.exitonclick()