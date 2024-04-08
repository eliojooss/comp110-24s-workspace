"""Draw a stary sky with Turtle!"""

__author__ = "Your PID"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Main drawing."""
    elio: Turtle = Turtle()
    elio.speed(10)
    background(elio, -200, -150)
    moon(elio, 125, 125)
    draw_stars(elio, -180, 180, 20, 4)
    lamp(elio, 80, -50)
    lamp(elio, -130, -50)
    elio.hideturtle()
    done()


def moon(turtle: Turtle, x: float, y: float) -> None:
    """Draw a moon."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('lightgray')
    turtle.fillcolor('lightgray')
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()


def box(turtle: Turtle, x_len: int, y_len: int, color: str) -> None:
    """Draw a rectangle."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(x_len)
        turtle.left(90)
        turtle.forward(y_len)
        turtle.left(90)
    turtle.end_fill()
        

def background(turtle: Turtle, x: float, y: float) -> None:
    """Draw the background, above and beyond using the box function to simplify repetitions."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('darkgreen')
    box(turtle, 400, 80, 'darkgreen')
    turtle.up()
    turtle.goto(x, y + 80)
    turtle.down()
    turtle.color('white')
    box(turtle, 80, 20, 'darkgray')
    turtle.goto(x + 80, y + 80)
    box(turtle, 160, 20, 'darkgray')
    turtle.goto(x + 160, y + 80)
    box(turtle, 80, 20, 'darkgray')
    turtle.goto(x + 240, y + 80)
    box(turtle, 80, 20, 'darkgray')
    turtle.goto(x + 320, y + 80)
    box(turtle, 80, 20, 'darkgray')
    turtle.up()
    turtle.goto(x, y + 100)
    turtle.down()
    turtle.color('darkblue')
    box(turtle, 400, 300, 'darkblue')


def star(turtle: Turtle, x: int, y: int, size: int) -> None:
    """Draw a star, above and beyond using some math, the interior angles of a 5 line star must add up to 180 and 36x5 = 180 and 180-36 = 144."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color((255, 255, 100))
    turtle.fillcolor((255, 255, 100))
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def draw_stars(turtle: Turtle, x: int, y: int, size: int, count: int) -> None:
    """Draw four stars, using recursion, Above and beyond, calling star function within draw stars to simplify the process."""
    if count == 0:
        return
    else:
        star(turtle, x, y, size)

        if count == 4:
            draw_stars(turtle, x + 140, y, size, count - 1)
        elif count == 3:
            draw_stars(turtle, x - 70, y + 30, size, count - 1)
        elif count == 2: 
            draw_stars(turtle, x, y - 60, size, count - 1)


def lamp(turtle: Turtle, x: int, y: int) -> None:
    """Draw a street lamp, above and beyond implementing box again."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black')
    box(turtle, 10, 125, 'black')
    turtle.up()
    turtle.goto(x + 5, y + 125)
    turtle.down()
    turtle.color('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


main()