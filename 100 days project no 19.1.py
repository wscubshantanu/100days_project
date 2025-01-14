from turtle import Turtle ,Screen

tim = Turtle()
screen = Screen()


def move0_forwards():
    tim.forward(100)

def move0_backwards():
    tim.backward(50)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move0_forwards,"w")
screen.onkey(move0_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.exitonclick()