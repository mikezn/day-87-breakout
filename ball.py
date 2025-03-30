from turtle import Turtle
import random

MOVE_DIST = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_dir = -1 if random.randint(1, 9)%2 == 0 else 1 # used to randomly choose the x direction at start
        self.y_dir = 1


    def move_ball(self):
        new_x = self.xcor() + (MOVE_DIST * self.x_dir)
        new_y = self.ycor() + (MOVE_DIST * self.y_dir)
        self.goto(new_x, new_y)

    def bounce(self, axis):
        if axis == "y":
            self.y_dir *= -1
        else:
            self.x_dir *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce("x")
