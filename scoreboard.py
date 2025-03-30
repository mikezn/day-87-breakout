from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.xpos = x
        self.ypos = y
        self.update_score()


    def point(self):
        self.score += 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(self.xpos, self.ypos)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def final_score(self):
        self.clear()
        self.goto(self.xpos, self.ypos)
        self.write(f'GAME OVER: {self.score}', align=ALIGNMENT, font=FONT)