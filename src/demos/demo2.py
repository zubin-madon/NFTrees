import random
import turtle

# __pragma__ ('skip')
# This is just to silence the Python linter not knowing about JS objects (Transcrypt ignores it)
class document:
    getElementById = None
# __pragma__ ('noskip')


def draw_tree(size, my_turtle):
    my_turtle.pensize(size / 20)

    if size < random.randint(1, 2) * 20:
        my_turtle.color("green")
    else:
        my_turtle.color("brown")

    if size > 5:
        my_turtle.forward(size)
        my_turtle.left(25)
        draw_tree(size - random.randint(10, 20), my_turtle)
        my_turtle.right(50)
        draw_tree(size - random.randint(10, 20), my_turtle)
        my_turtle.left(25)
        my_turtle.up()  # penup()
        my_turtle.back(size)  # backward(size)
        my_turtle.down()  # pendown()


def tree(size):
    if size < 10:
        size = 10
    if size > 200:
        size = 200
    document.getElementById("size").value = size

    turtle.reset()
    turtle.bgcolor("#DDDDDD")

    my_turtle = turtle.Turtle()
    my_turtle.clear()
    my_turtle.color("brown", "blue")
    my_turtle.left(90)
    my_turtle.speed(0)
    my_turtle.up()  # penup()
    my_turtle.goto(0, size * 2)  # setpos(0, -250)
    my_turtle.down()  # pendown()

    draw_tree(size, my_turtle)

    my_turtle.done()  # display


def attach_turtle():
    turtle.setDefaultElement(document.getElementById('root'))
