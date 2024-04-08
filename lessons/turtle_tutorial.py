from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(0, 0)
leo.pendown()
 
i: int = 0
for i in range(2):
    leo.forward(300)
    leo.left(90)
    leo.forward(100)
    leo.left(90)
    i = i + 1

done()