from turtle import *
import random
is_race_on=False
colors=["red","blue","pink","yellow","purple","green"]
screen=Screen()
screen.setup(500,400)
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]
user_bet=screen.textinput(title="Make a Bet",prompt="Which turtle will win?,Enter a colour:")
for index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_pos[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"YOU WIN,CORRECT BET")
            else:
                print(f"WRONG BET {winning_color} is the real winner")


        dist=random.randint(1,10)
        turtle.forward(dist)
        turtle.speed(0)
screen.clear()
screen.exitonclick()
