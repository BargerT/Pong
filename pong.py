import turtle
from tkinter import *
import tkinter as tk

h = 600
w = 1000

ai_speed = 1
ai_predict = False

# Create Screen
sc = turtle.Screen()
canvas = sc.getcanvas()
sc.title("Pong Game")
sc.bgcolor("Black")
sc.setup(width=w, height=h)
var = tk.IntVar()


# Button Click Functionality
def easyClick():
    global ai_speed
    ai_speed = 0.2
    var.set(1)


def normalClick():
    global ai_speed
    ai_speed = 1
    var.set(1)


def hardClick():
    global ai_speed
    ai_speed = 2
    var.set(1)


def impossibleClick():
    global ai_speed
    global ai_predict
    ai_speed = 5
    ai_predict = True
    var.set(1)


# Menu Buttons
canvas = sc.getcanvas()
easy = Button(canvas.master, text="Easy", command=easyClick)
normal = Button(canvas.master, text="Normal", command=normalClick)
hard = Button(canvas.master, text="Hard", command=hardClick)
impossible = Button(canvas.master, text="Impossible", command=impossibleClick)

easy.pack()
normal.pack()
hard.pack()
impossible.pack()

easy.place(x=w / 2, y=(h / 5) * 4)
normal.place(x=w / 2, y=(h / 5) * 3)
hard.place(x=w / 2, y=(h / 5) * 2)
impossible.place(x=w / 2, y=(h / 5))

canvas.wait_variable(var)

easy.destroy()
normal.destroy()
hard.destroy()
impossible.destroy()

# Left Paddle
left_p = turtle.Turtle()
left_p.speed(0)
left_p.shape("square")
left_p.color("white")
left_p.shapesize(stretch_wid=6, stretch_len=2)
left_p.penup()
left_p.goto(-((w / 2) - 100), 0)

# Right Paddle
right_p = turtle.Turtle()
right_p.speed(0)
right_p.shape("square")
right_p.color("white")
right_p.shapesize(stretch_wid=6, stretch_len=2)
right_p.penup()
right_p.goto(((w / 2) - 100), 0)

# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Score
left_player = 0
right_player = 0

# Score Display
sboard = turtle.Turtle()
sboard.speed(0)
sboard.color("white")
sboard.penup()
sboard.hideturtle()
sboard.goto(0, ((h / 2) - 40))
sboard.write("Opponent: 0    Player: 0", align="center", font=("Courier", 24, "normal"))


# Moving the paddles
def LeftPaddleUp():
    y = left_p.ycor()
    y += 20 * ai_speed
    left_p.sety(y)


def LeftPaddleDown():
    y = left_p.ycor()
    y -= 20 * ai_speed
    left_p.sety(y)


def RightPaddleUp():
    y = right_p.ycor()
    y += 20
    right_p.sety(y)


def RightPaddleDown():
    y = right_p.ycor()
    y -= 20
    right_p.sety(y)


# Keybinds
sc.listen()
sc.onkeypress(RightPaddleUp, "Up")
sc.onkeypress(RightPaddleDown, "Down")


while True:
    sc.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # AI Controls
    if left_p.ycor() < ball.ycor() and abs(left_p.ycor() - ball.ycor()) > 10:
        LeftPaddleUp()

    elif left_p.ycor() > ball.ycor() and abs(left_p.ycor() - ball.ycor()) > 10:
        LeftPaddleDown()

    # Check the Edges
    if ball.ycor() > ((h / 2) - 20):
        ball.sety(((h / 2) - 20))
        ball.dy *= -1

    if ball.ycor() < -((h / 2) - 20):
        ball.sety(-((h / 2) - 20))
        ball.dy *= -1

    if ball.xcor() > (w / 2):
        ball.goto(0, 0)
        ball.dy = -5
        ball.dx = 5
        left_player += 1
        sboard.clear()
        sboard.write(
            "Opponent: {}   Player: {}".format(left_player, right_player),
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < (-(w / 2)):
        ball.goto(0, 0)
        ball.dy = -5
        ball.dx = 5
        right_player += 1
        sboard.clear()
        sboard.write(
            "Opponent: {}   Player: {}".format(left_player, right_player),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Make the Paddles Hit the Ball
    if (ball.xcor() > right_p.xcor() - 40 and ball.xcor() < right_p.xcor()) and (
        ball.ycor() < right_p.ycor() + 60 and ball.ycor() > right_p.ycor() - 60
    ):
        ball.setx(((w / 2) - 140))
        ball.dx *= -1.1

    if (ball.xcor() < left_p.xcor() + 40 and ball.xcor() > left_p.xcor()) and (
        ball.ycor() < left_p.ycor() + 60 and ball.ycor() > left_p.ycor() - 60
    ):
        ball.setx(-((w / 2) - 140))
        ball.dx *= -1.1
