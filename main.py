from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("skyblue")
screen.colormode(255)

def random_color():
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    random_color = (r, g, b)
    return random_color 

"""Square"""
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)
# tim.forward(5)

"""Dotted Line"""
# for _ in range(10):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()
#     tim.forward(5)
# screen.colormode(255)


"""Triangle->Octagon"""
# sum = 0
# n = 3
# while sum < 8:
#     tim.color(random_color)
#     tim.pencolor(r,g,b)
#     x = 360 / n
#     for i in range(n):
#         tim.right(x)
#         tim.forward(100)
#     n += 1
#     sum += 1



"""Random Art Work"""
# movements = [tim.forward(100) , tim.back(100), tim.right(90), tim.left(90)]
# screen.colormode(255)
# tim.pensize(10)
# tim.speed(5)
# for _ in range(200):
#     r = int(randint(1,255))
#     b = int(randint(1,255))
#     g = int(randint(1,255))
#     tim.pencolor(r,g,b)
#     r = randint(0, 3)
#     if r == 0:
#         tim.forward(25)
#     elif r == 1:
#         tim.back(25)
#     elif r == 2:
#         tim.right(90)
#         tim.forward(25)
#     elif r == 3:
#         tim.left(90)
#         tim.forward(25)


# tim.pensize(10)
# tim.speed(5)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random_color())
#     tim.pencolor()
#     tim.forward(30)
#     tim.setheading(choice(directions))


# tim.shape('arrow')
# tim.speed("fastest")

# def draw(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
        
# draw(6)


screen = Screen()
screen.exitonclick()