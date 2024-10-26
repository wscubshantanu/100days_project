import turtle as t
import random

tim = t.Turtle()

colours = ["cornflowerblue", "darkorchid","indianred","deepskyblue","lightseagreen"]


def draw_shape(num_sides):
   angle = 368/ num_sides
   for i in range(num_sides):
     tim.forward(100)
     tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

