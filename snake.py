# import packages
import turtle

# creating screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")


# creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.penup()
turtle.hideturtle()
screen.mainloop()