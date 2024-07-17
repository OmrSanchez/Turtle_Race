from turtle import Turtle, Screen
import random

screen = Screen()
grn_t = Turtle()
pnk_t = Turtle()
blk_t = Turtle()
orng_t = Turtle()
ppl_t = Turtle()
blu_t = Turtle()
finish = Turtle()
post_1 = Turtle()
post_2 = Turtle()

screen.setup(width=1400, height=500)

post_1.teleport(x=615, y=150)
post_1.shape("circle")
post_1.color("maroon")

post_2.teleport(x=615, y=-200)
post_2.shape("circle")
post_2.color("maroon")

finish.hideturtle()
finish.teleport(x=615, y=150)
finish.setheading(270)
finish.pd()
finish.pensize(3)
finish.color("black")
finish.fd(350)

grn_t.resizemode("user")
grn_t.shapesize(1.5, 1.5, 1.5)
grn_t.color('green')
grn_t.shape('turtle')
grn_t.pu()
grn_t.setposition(x=-600, y=100)
grn_t.speed("fastest")

pnk_t.resizemode("user")
pnk_t.shapesize(1.5, 1.5, 1.5)
pnk_t.color('pink')
pnk_t.shape('turtle')
pnk_t.pu()
pnk_t.setposition(x=-600, y=50)
pnk_t.speed("fastest")

blk_t.resizemode("user")
blk_t.shapesize(1.5, 1.5, 1.5)
blk_t.color('black')
blk_t.shape('turtle')
blk_t.pu()
blk_t.setposition(x=-600, y=0)
blk_t.speed("fastest")

orng_t.resizemode("user")
orng_t.shapesize(1.5, 1.5, 1.5)
orng_t.color('orange')
orng_t.shape('turtle')
orng_t.pu()
orng_t.setposition(x=-600, y=-50)
orng_t.speed("fastest")

ppl_t.resizemode("user")
ppl_t.shapesize(1.5, 1.5, 1.5)
ppl_t.color('purple')
ppl_t.shape('turtle')
ppl_t.pu()
ppl_t.setposition(x=-600, y=-100)
ppl_t.speed("fastest")

blu_t.resizemode("user")
blu_t.shapesize(1.5, 1.5, 1.5)
blu_t.color('blue')
blu_t.shape('turtle')
blu_t.pu()
blu_t.setposition(x=-600, y=-150)
blu_t.speed("fastest")

turtle_list = [grn_t, pnk_t, blk_t, orng_t, ppl_t, blu_t]
turtle_pos = []

user_bet = screen.textinput("BET", "Who will win? (green, pink, black, orange, purple, blue): ").lower()

race_on = True
while race_on:
    for t in turtle_list:
        if t.pos()[0] < 600:
            t.fd(random.randint(0, 10))
        else:
            race_on = False
for i in turtle_list:
    turtle_pos.append(i.pos()[0])
furthest = max(turtle_pos)
for i in turtle_list:
    if i.pos()[0] == furthest:
        winner = i.color()[0].lower()
if user_bet == winner:
    print(f"The winner is {winner}. Amazing! You win!")
    race_on = False
else:
    print(f"The winner is {winner}. You lose.")
    race_on = False


screen.exitonclick()
