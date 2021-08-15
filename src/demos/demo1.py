from turtle import Turtle


josh = Turtle()

# __pragma__ ('ecom')
'''?
from turtle import _svg, _ns, _offset
def write(self, txt):
    print(txt)
    console.log(self.pos())
    text = document.createElementNS(_ns, 'text')
    text.setAttribute ('x', self.pos()[0] + _offset[0])
    text.setAttribute ('y', self.pos()[1] + _offset[1])
    text.innerHTML = txt
    _svg.appendChild(text)

josh.write = lambda txt: write(josh, txt)
?'''
# __pragma__ ('noecom')


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
        josh.write(f'{i}')
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

