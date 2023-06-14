import turtle
import time  # new import for delaying
import tkinter as tk
from tkinter import messagebox

# Set up screen
win = turtle.Screen()
win.title("Brick Breaker")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Variables for paddle movement
move_speed = 1.5
left_pressed = False
right_pressed = False

# Functions
def paddle_left():
    global left_pressed
    left_pressed = True

def paddle_right():
    global right_pressed
    right_pressed = True

def paddle_left_release():
    global left_pressed
    left_pressed = False

def paddle_right_release():
    global right_pressed
    right_pressed = False

def game_over(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = messagebox.askyesno("Game Over", message + "\nPlay Again?")
    root.destroy()  # Close the main window

    if result:
        play_again_yes()
    else:
        play_again_no()

def play_again_yes():
    global play_again
    play_again = True
    

def play_again_no():
    global play_again
    play_again = False
    
play_again = True
while play_again:
    play_again = False

play_again = True
while play_again:
    play_again = False

# Keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")
win.onkeyrelease(paddle_left_release, "Left")
win.onkeyrelease(paddle_right_release, "Right")

play_again = True
while play_again:
    play_again = False
    
    # Paddle
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -250)

    # Ball
    ball = turtle.Turtle()
    ball.speed(1)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.25
    ball.dy = -0.25

    #lives
    lives = 3

    # Lives display
    lives_display = turtle.Turtle()
    lives_display.speed(0)
    lives_display.color("white")
    lives_display.penup()
    lives_display.showturtle()  
    lives_display.goto(-370, 260)
    lives_display.write("Lives: {}".format(lives), align="left", font=("Courier", 24, "normal"))

    # Bricks
    bricks = []
    for i in range(6):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("red")
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-270 + (i*100), 250)
        bricks.append(brick)

    # Main game loop
    while True:
        win.update()

        # Paddle movement
        if left_pressed and paddle.xcor() > -350:
            paddle.setx(paddle.xcor() - move_speed)

        if right_pressed and paddle.xcor() < 350:
            paddle.setx(paddle.xcor() + move_speed)
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision
        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.goto(0, 0)
            ball.dy *= -1
            lives -= 1
            lives_display.clear()
            lives_display.write("Lives: {}".format(lives), align="left", font=("Courier", 24, "normal"))

        # Paddle collision
        if (ball.dy < 0) and (-240 < ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
            ball.dy *= -1

        # Brick collision
        for brick in bricks:
            if abs(brick.xcor() - ball.xcor()) < 35 and abs(brick.ycor() - ball.ycor()) < 20:
                brick.goto(1000, 1000)  # Move hit bricks out of the way
                ball.dy *= -1
                bricks.remove(brick)

        # Check for game over
        if lives <= 0:
            game_over("Game Over")
            break

        # Check for win
        if len(bricks) == 0:
            game_over("You Win!")
            break

    # Clean up game objects when the game is over
    paddle.clear()
    paddle.hideturtle()
    ball.clear()
    ball.hideturtle()
    lives_display.clear()  
    lives_display.hideturtle()  
    for brick in bricks:
        brick.clear()
        brick.hideturtle()


