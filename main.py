#GAME STARTS WHEN YOU PRESS ANY ARROW 




import turtle
import time
import random

DELAY = 0.1  # to control the speed of the game


win = turtle.Screen()  # sets up the game window
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off the screen updates

# Score display
score_display = turtle.Turtle()       # to display the score at the top of the window
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Initialize score
score = 0

# Functions
def display_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def game_over():
    global score
    win.onkeypress(None, "Up")
    win.onkeypress(None, "Down")
    win.onkeypress(None, "Left")
    win.onkeypress(None, "Right")
    win.update()
    score_display.clear()
    score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def check_collision():
    global score
    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 1
        display_score()

    # Check for collision with walls
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

    # Check for collision with the snake's own body
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the snake
    move()

    # Check for collisions
    check_collision()

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    time.sleep(DELAY)