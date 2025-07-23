from turtle import Turtle, Screen
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
MOVE_RANGE = (0, 10)


def move_turtles(p_turtles):
    for t in p_turtles:
        t.forward(random.randint(MOVE_RANGE[0], MOVE_RANGE[1]))


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput("Make your bet", "Enter the color of turtle you think will win this race.")
turtles = []

for i, col in enumerate(colors):
    t = Turtle(shape="turtle")
    t.penup()
    turtles.append(t)
    t.color(col)
    t.goto(-SCREEN_WIDTH / 2 + 20, (i * 20) - 50)


race_on = True

while race_on:
    move_turtles(turtles)
    for i, t in enumerate(turtles):
        if t.xcor() > 20:
            print(f"The winner is color {colors[i]}")
            if colors[i] == user_bet:
                print("YOU WIN.")
            else:
                print("YOU LOST. GAME OVER.")
            race_on = False


screen.exitonclick()
