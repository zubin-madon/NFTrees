import gzip
import math
import xml.etree.ElementTree as ET


class Turtle:
    DEFAULT_WIDTH = 100
    DEFAULT_HEIGHT = 100

    _svg = ET.Element("svg")

    _width = DEFAULT_WIDTH
    _height = DEFAULT_HEIGHT
    _offset = [_width // 2, _height // 2]

    _allTurtles = []

    @classmethod
    def __str__(cls):
        return ET.tostring(cls._svg, encoding='utf-8').decode('utf-8')

    @classmethod
    def write_file(cls, filename: str, compress: bool = False):
        if compress:
            with gzip.open(filename, 'wb') as f:
                ET.ElementTree(cls._svg).write(f)
        else:
            ET.ElementTree(cls._svg).write(filename)

    @classmethod
    def flush(cls):
        for turtle in cls._allTurtles:
            turtle._flush()

    @classmethod
    def reset(cls):
        _width = cls.DEFAULT_WIDTH
        _height = cls.DEFAULT_HEIGHT
        _offset = [0, 0]

        for turtle in cls._allTurtles:
            turtle._heading = math.pi / 2
            turtle._track = []
            turtle.pensize(1)
            turtle.color('black', 'black')
            turtle.up()
            turtle.home()

        cls.clear()

    @classmethod
    def clear(cls):
        for turtle in cls._allTurtles:
            turtle._track = []
            turtle._moveto(turtle._position)

        cls.setup()

    @classmethod
    def setup(cls, width=_width, height=_width):
        cls._width = width
        cls._height = height
        cls._offset = [cls._width // 2, cls._height // 2]

        cls._svg = ET.Element("svg")
        cls._svg.attrib['width'] = str(cls._width)
        cls._svg.attrib['height'] = str(cls._height)
        # cls.svg.attrib['fill'] = "none"
        cls._svg.attrib['viewBox'] = f"0 0 {cls._width} {cls._height}"
        cls._svg.attrib['xmlns'] = "http://www.w3.org/2000/svg"

    def __init__(self):
        self.__class__._allTurtles.append(self)

        self._pensize = 1
        self._pencolor = "black"
        self._fillcolor = "black"
        self._fill = False
        self._position = [self.__class__._width // 2, self.__class__._height // 2]
        self._heading = math.pi / 2
        self._down = False
        self._track = []

        self.pencolor = self.color
        self.penup = self.up
        self.pendown = self.down
        self.width = self.pensize
        self.backward = self.back

        self.home()

    def _flush(self):
        if len(self._track) > 1:
            path = ET.SubElement(self.__class__._svg, "path")
            path.attrib['d'] = ' '.join(self._track)
            path.attrib['stroke'] = self._pencolor if self._pencolor is not None else 'none'
            path.attrib['stroke-width'] = str(self._pensize)
            path.attrib['fill'] = self._fillcolor if self._fill and self._fillcolor is not None else 'none'
            path.attrib['fill-rule'] = 'evenodd'

            self._track = []
            self._moveto(self._position)  # _track should start with a move command

    def done(self):
        self._flush()

    def pensize(self, width):
        self._flush()
        if width is None:
            return self._pensize
        else:
            self._pensize = width

    def bgcolor(self, background_color):
        self.rect(self.__class__._width, self.__class__._height, background_color)

    def color(self, pencolor, fillcolor=None):
        self._flush()
        self._pencolor = pencolor

        if fillcolor is not None:
            self._fillcolor = fillcolor

    def goto(self, x, y=None):
        if y is None:
            self._position = x
        else:
            self._position = [x, -y]

        self._track.append('{} {} {}'.format(
            'L' if self._down else 'M',
            self._position[0] + self.__class__._offset[0],
            self._position[1] + self.__class__._offset[1])
        )

    def _moveto(self, x, y=None):
        wasdown = self.isdown()
        self.up()
        self.goto(x, y)
        if wasdown:
            self.down()

    def home(self):
        # self._moveto(self.__class__._width // 2, self.__class__._height // 2)
        self._moveto(0, 0)

    def position(self):
        return self._position[:]

    def pos(self):
        return self.position()

    def distance(self, x, y=None):
        if y is None:
            other = x
        else:
            other = [x, y]

        dX = other[0] - self._position[0]
        dY = other[1] - self._position[1]

        return math.sqrt(dX * dX + dY * dY)

    def up(self):
        self._down = False

    def down(self):
        self._down = True

    def isdown(self):
        return self._down

    def _predict(self, length):
        delta = [math.sin(self._heading), math.cos(self._heading)]
        return [self._position[0] + length * delta[0], self._position[1] + length * delta[1]]

    def forward(self, length):
        self._position = self._predict(length)

        self._track.append('{} {} {}'.format(
            'L' if self._down else 'M',
            self._position[0] + self.__class__._offset[0],
            self._position[1] + self.__class__._offset[1])
        )

    def back(self, length):
        self.forward(-length)

    def rect(self, width, height, fill_color):
        bg = ET.SubElement(self.__class__._svg, "rect")
        bg.attrib['width'] = str(width)
        bg.attrib['height'] = str(height)
        bg.attrib['fill'] = fill_color

    def circle(self, radius):
        self.left(90)
        opposite = self._predict(2 * (radius + 1) + 1)
        self.right(90)

        self._track.append('{} {} {} {} {} {} {} {}'.format(
            'A',
            radius,
            radius,
            0,
            1,
            0,
            opposite[0] + self.__class__._offset[0],
            opposite[1] + self.__class__._offset[1]
        ))

        self._track.append('{} {} {} {} {} {} {} {}'.format(
            'A',
            radius,
            radius,
            0,
            1,
            0,
            self._position[0] + self.__class__._offset[0],
            self._position[1] + self.__class__._offset[1]
        ))

    def left(self, angle):
        self._heading = (self._heading + math.pi * angle / 180) % (2 * math.pi)

    def right(self, angle):
        self.left(-angle)

    def begin_fill(self):
        self._flush()
        self._fill = True

    def end_fill(self):
        self._flush()
        self._fill = False

    def speed(self, val=None):
        pass

    def write(self, txt, font=None, align='center'):
        if not font:
            font = ('sans-serif', 14, 'bold')

        text = ET.SubElement(self.__class__._svg, "text")
        text.attrib['x'] = str(self.pos()[0] + self.__class__._offset[0])
        text.attrib['y'] = str(self.pos()[1] + self.__class__._offset[1])
        text.attrib['fill'] = self._pencolor
        # text.attrib['align'] = align
        text.attrib['style'] = f'font-size:{font[1] * 1.5}px; font-weight:{font[2]}; font-family:{font[0]}, sans-serif;'
        text.text = str(txt)

    @staticmethod
    def hideturtle():
        pass

    @staticmethod
    def shape(val):
        pass

    def mainloop(self):
        self.write_file('test.svg')

    def update(self):
        self._flush()


def delay(val):
    pass


def tracer(val):
    pass


def bgcolor(val):
    pass


def reset():
    pass


if __name__ == '__main__':
    svg = Turtle()
    svg.setup(160, 100)
    # svg.style("path {stroke-width: 12; stroke-linecap: round} text {font: bold 20px sans-serif;}")
    svg.rect(svg._width, svg._height, "black")
    svg.goto(10, 30)
    svg.color("yellow")
    svg.write("hello")
    print(svg)

