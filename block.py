from turtle import Turtle

class Block(Turtle):
    def __init__(self, xy, block_width, block_height, colour):
        super().__init__()
        self.block_width = block_width/20 # div by 20 as turtle works in divisions of 20px
        self.block_height = block_height/20 # div by 20 as turtle works in divisions of 20px
        self.shape("square")
        self.color(colour)
        self.turtlesize(stretch_wid=self.block_height, stretch_len=self.block_width)
        self.penup()
        self.goto(xy)

    def collides_with(self, ball):
        bx, by = ball.xcor(), ball.ycor()
        x, y = self.xcor(), self.ycor()
        bw, bh = (self.block_width*20) / 2, (self.block_height*20) / 2
        radius = 10  # adjust if your ball is larger

        # Check if ball is overlapping block
        if (x - bw - radius <= bx <= x + bw + radius) and \
                (y - bh - radius <= by <= y + bh + radius):

            # Calculate overlap in x and y
            dx = min(abs(bx - (x - bw)), abs(bx - (x + bw)))
            dy = min(abs(by - (y - bh)), abs(by - (y + bh)))

            # Return which direction the collision likely came from
            if dx < dy:
                return "x"  # hit side → bounce horizontally
            else:
                return "y"  # hit top/bottom → bounce vertically

        return None  # no collision
