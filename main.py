# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 19 - Intermediate - Python Turtles Drawing
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def rotate_clockwise():
    timmy.right(10)

def rotate_counterclockwise():
    timmy.left(10)

def clear_screen():
    timmy.reset() # clear and home function can be used instead

# Challenge, when pressed indicated letter turtle should perform specified function:
# W = Forward
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear and back in the center

screen.listen()
# Higher Order Functions are functions that can work with other functions, can be done Python, but every language
# It's recommended to use keywords for passing to things to a functions when position doesn't really have meaning
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()