from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xy, paddle_width, paddle_height):
        super().__init__()
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.paddle_height, stretch_len=self.paddle_width)
        self.penup()
        self.goto(xy)

    def move_left(self):
        self.goto(self.xcor() -20, self.ycor())

    def move_right(self):
        self.goto(self.xcor() +20, self.ycor())

    def move_paddle(self, x):
        self.setx(x)