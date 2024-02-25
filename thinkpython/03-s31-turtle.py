"""Excercises 1-5
Use the turtle module to draw a circle with the radius r
Make a more general version of circle() called arc() that takes an additional
parameter angle, which determines what fraction of a circle to draw."""

import turtle
from math import pi

my_turtle = turtle.Turtle()

def draw_arc(t, length, segments, angle):
    for i in range(segments):
        t.fd(length)
        t.lt(angle)

def arc(t, r, a):
    circumference = 2 * pi * r
    arc = circumference * a / 360
    number_s = int(arc / 3) + 3
    angle = a / number_s
    length_s = arc / number_s
    draw_arc(t, length_s, number_s, angle)

def circle(t, r):              # Can be refactored to call arc(t, r, 360)
    arc(t, r, 360)
    """circumference = 2 * pi * r
    number_s = int(circumference / 3) + 3
    length_s = circumference / number_s
    polygons(t, length_s, number_s, number_s)"""

if __name__=="__main__":
    circle(my_turtle, 80)
    arc(my_turtle, 100, 270)
    turtle.mainloop()