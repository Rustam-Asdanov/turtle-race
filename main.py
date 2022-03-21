from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("lightblue")
screen.title("Turtle race!")

color_triple = ("red", "blue", "green", "yellow", "black", "purple")
turtles_list = []
start = 130


def create_turtle():
    for c in range(len(color_triple)):
        t = Turtle()
        t.shape("turtle")
        t.color(color_triple[c])
        t.penup()
        t.setposition(-230, start - 50 * c)
        turtles_list.append(t)


def get_turtles():
    return turtles_list


def turtle_move(turtle):
    random_num = random.randint(0, 30)
    turtle.forward(random_num)


def start_game():
    user_choice = screen.textinput(title="Make your bet",
                                   prompt="Which turtle will win the race? Enter a color: ")
    game_over = False
    winner_color = ""
    while not game_over:
        for turtle in get_turtles():
            turtle_move(turtle)
            if turtle.position()[0] > 200:
                game_over = True
                winner = turtle.color()[0]

    if user_choice == winner_color:
        print("You are winner!")
    else:
        print("You are loser!")


create_turtle()
start_game()

screen.exitonclick()
