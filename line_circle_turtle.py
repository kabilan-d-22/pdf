import turtle
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Line and Circle Drawing")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

PIXEL_SIZE = 10

def set_pixel(x, y, color="black"):
    pen.goto(x, y)
    pen.dot(PIXEL_SIZE, color)

def draw_line(x1, y1, x2, y2, color="blue"):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        set_pixel(round(x), round(y), color)
        x += x_inc
        y += y_inc
        time.sleep(0.005)

def draw_circle(cx, cy, r, color="green"):
    x = 0
    y = r
    p = 1 - r

    def plot_points(xc, yc, x, y):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            set_pixel(px, py, color)

    plot_points(cx, cy, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_points(cx, cy, x, y)
        time.sleep(0.01)

# Set coordinate system so (0,0) is center of screen
screen.setworldcoordinates(-350, -350, 350, 350)

# Draw line first
draw_line(-150, -150, 150, 150)

# Draw circle centered at (0,0)
draw_circle(0, 0, 100)

screen.exitonclick()
