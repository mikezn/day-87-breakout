import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 855
SCREEN_HEIGHT = 600

WALL_LEFT = ((SCREEN_WIDTH/2)*-1)
WALL_RIGHT = SCREEN_WIDTH/2
WALL_TOP = (SCREEN_HEIGHT/2)-100
WALL_BOTTOM = ((SCREEN_HEIGHT/2)*-1)

# Set up screen
screen = Screen()
screen.title("BREAKOUT")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Create new player
player = Paddle((0, WALL_BOTTOM+15), paddle_width=5, paddle_height=1)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard(0, WALL_TOP-20)

screen.listen()
# player paddle to follow mouse
screen.onscreenclick(lambda x, y: None)  # Optional: force focus on screen
screen.getcanvas().bind("<Motion>", lambda event: player.move_paddle(event.x - SCREEN_WIDTH / 2))

# player paddle to move on arrow key press
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Create blocks
blocks = []

# Block layout
rows = 1
cols = 1
block_width = 80
block_height = 20
spacing =  5
start_x = WALL_LEFT + (block_width/2)
start_y = WALL_TOP - (block_height/2)

# generate blocks
for row in range(rows):
    for col in range(cols):
        x = start_x + col * (block_width + spacing)
        print(x)
        y = start_y - row * (block_height + spacing)
        print(y)
        block = Block((x, y), block_width, block_height, "white")
        blocks.append(block)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move_ball()

    #COLLISSION DETECT top
    if ball.ycor() > WALL_TOP-20:
        ball.bounce("y")

    if ball.xcor() < WALL_LEFT+20 or ball.xcor() > WALL_RIGHT-20:
        ball.bounce("x")

    #COLLISSION DETECT paddle
    if ball.distance(player) < 50 and ball.ycor() < (WALL_BOTTOM+35):
        ball.bounce("y")

    #DETECT BALL MISS AT BOTTOM
    if ball.ycor() < WALL_BOTTOM:
        ball.reset_position()

    #COLLISION DETECT block
    # This special 'for' creates a shallow copy of blocks so blocks can be safely removed from the original list without
    # altering the list size we're looping through
    print(len(blocks))
    if len(blocks) > 0:
        for block in blocks[:]:
                collide = block.collides_with(ball)
                if not collide:
                    pass
                else:
                    ball.bounce(collide)
                    block.hideturtle()
                    blocks.remove(block)
                    scoreboard.point()
    else:
        scoreboard.final_score()
        game_is_on = False


screen.exitonclick()