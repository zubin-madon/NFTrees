from turtle import Turtle


josh = Turtle()


def draw(length):
    if length > 9:
        draw(length / 3)
        josh.left(60)
        draw(length / 3)
        josh.right(120)
        draw(length / 3)
        josh.left(60)
        draw(length / 3)
    else:
        josh.forward(length)


def main(screen=None):
    josh.speed('fastest')
    length = 150
    josh.up()
    josh.forward(length / 2)
    josh.left(90)
    josh.forward(length / 4)
    josh.right(90)
    josh.down()

    for i in range(3):
        josh.right(120)
        draw(length)

    if screen:
        screen.mainloop()
    else:
        josh.done()


if __name__ == '__main__':
    scr = None
    # __pragma__ ('skip')

    from turtle import Screen
    scr = Screen()
    scr.setup(width=900, height=900)
    scr.bgcolor('white')
    # __pragma__ ('noskip')

    main(scr)

