from turtle import Turtle
import random


# Transcrypt random does not have randrange so we monkeypatch it
# __pragma__ ('ecom')
'''?
def random_randrange(start, end, step):
    rand = random.randint(start, end-1)
    adj_rand = rand - (rand%step) + (start%step)
    # print(start, end, step, rand, adj_rand)
    return adj_rand

random.randrange = random_randrange
?'''
# __pragma__ ('noecom')

# Transcrypt turtle does not have write so we monkeypatch it
# __pragma__ ('ecom')
'''?
from turtle import _svg
from turtle import _ns
from turtle import _offset

def turtle_write(self, txt):
    text = document.createElementNS(_ns, 'text')
    text.setAttribute ('x', self.pos()[0] + _offset[0])
    text.setAttribute ('y', self.pos()[1] + _offset[1])
    text.innerHTML = txt
    _svg.appendChild(text)
?'''
# __pragma__ ('noecom')


LEAF_STYLE = ('RootBeer', 10, 'bold')
ROOT_STYLE = ('RootBeer', 10, 'bold')
LABEL_STYLE = ('RootBeer', 14, 'bold')


# __pragma__ ('kwargs')
class TreeBuilder:
    def __init__(self, seq):
        self.seq = seq

    # --- pseudo "randomizer" functions based on predefined sequence
    def get_seq(self):
        for n in self.seq:
            yield n

    def choose(self, seq, lst):
        return lst[int(next(seq) * len(lst))]

    def choose_int(self, seq, start, end):
        return self.choose(seq, range(start, end + 1))

    def choose_range(self, seq, start, end, step):
        rand = self.choose(seq, range(start, end))
        adj_rand = rand - (rand % step) + (start % step)
        return adj_rand

    # --- Tree Functions--------

    def multi_turtle_tree(self, palette, LEAVES, angle_step):
        turtles_ = []
        for i in range(len(LEAVES)):
            tim = Turtle()
            tim.hideturtle()
            tim.up()
            tim.goto(0, -100)
            tim.left(90)
            tim.color("white")
# __pragma__ ('ecom')
            #?tim.write = lambda txt: turtle_write(nib, txt)
# __pragma__ ('noecom')
            turtles_.append(tim)

        for i in range(len(turtles_)):
            turtles_[i].down()
            turtles_[i].pensize(6)
            length1 = random.randrange(80, 180, 20)
            turtles_[i].forward(length1)
            angle1 = random.randrange(-55, 55, angle_step)
            turtles_[i].left(angle1)
            turtles_[i].pensize(3)
            length2 = length1 * 0.618
            turtles_[i].forward(length2)

            if random.random() <= 0.618:
                turtles_[i].pensize(2)
                if angle1 < 0:
                    angle2 = random.randrange(-42, -7, 14)
                    turtles_[i].left(angle2)
                if angle1 > 0:
                    angle2 = random.randrange(7, 42, 14)
                    turtles_[i].left(angle2)
                turtles_[i].forward(0.618 * length2)

                if random.random() <= 0.618:
                    turtles_[i].pensize(1)
                    if angle1 < 0:
                        angle2 = random.randrange(-60, 15, 15)
                        turtles_[i].left(angle2)
                    if angle1 > 0:
                        angle2 = random.randrange(15, 60, 15)
                        turtles_[i].left(angle2)
                    turtles_[i].forward(length2 * 0.618 * 0.618)
                    turtles_[i].color(random.choice(palette))
                    leaf = random.choice(LEAVES)
                    turtles_[i].write(leaf)
                    LEAVES.remove(leaf)
                    turtles_[i].color('white')

                else:
                    if len(LEAVES) == 0:
                        pass
                    else:
                        turtles_[i].color(random.choice(palette))
                        leaf = random.choice(LEAVES)
                        turtles_[i].write(leaf)
                        LEAVES.remove(leaf)
                        turtles_[i].color('white')

            else:
                if len(LEAVES) == 0:
                    pass
                else:
                    seq = self.get_seq()
                    turtles_[i].color(self.choose(seq, palette))
                    leaf = self.choose(seq, LEAVES)
                    turtles_[i].write(leaf)
                    LEAVES.remove(leaf)
                    turtles_[i].color('white')
                    return

    # ----------Symmetrical Tree--------------------------------------

    def sym_tree(self, nib_name, length, levels, angle, len_reduce, palette, LEAVES, pen_size):
        if len(LEAVES) == 0:
            nib_name.up()
            return

        nib_name.down()
        if levels == 0:
            return

        nib_name.pensize(pen_size)
        nib_name.forward(length)
        nib_name.right(angle)
        self.sym_tree(nib_name, length * len_reduce, levels - 1, angle, len_reduce, palette, LEAVES, pen_size * 0.6)
        nib_name.left(angle * 2)
        self.sym_tree(nib_name, length * len_reduce, levels - 1, angle, len_reduce, palette, LEAVES, pen_size * 0.6)
        nib_name.right(angle)
        
        if len(LEAVES) != 0:
            leaf = random.choice(LEAVES)
            nib_name.color(random.choice(palette))
            nib_name.write(leaf, font=LEAF_STYLE)
            nib_name.color('white')
            LEAVES.remove(leaf)

        nib_name.back(length)

    # -------------ASYMMETRIC TREE FUNCTION--------------------

    def asymmetric_tree_under14(self, nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
        if len(LEAVES) == 0:
            return
        nib_name.down()
        if levels == 0:
            return

        if levels >= 1:
            nib_name.down()

            seq = self.get_seq()
            if start or next(seq) > 0.5:
                nib_name.pensize(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                self.asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.right(angle)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.left(angle)
                nib_name.right(2 * angle)

                if len(LEAVES) == 0:
                    nib_name.up()
                    return
           
                leaf = random.choice(LEAVES)
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=LEAF_STYLE)
                LEAVES.remove(leaf)

                nib_name.color('white')
                nib_name.back(length)

    # -------------------------------------------------------------------------------------------------------------------

    def asymmetric_tree_under47(self, nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
        if len(LEAVES) == 0:
            return
        nib_name.down()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.down()
            seq = self.get_seq()
            if start or next(seq) > 0.5:
                nib_name.pensize(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                self.asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.right(angle)
                self.asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.left(angle)
                nib_name.right(2 * angle)

                if len(LEAVES) == 0:
                    nib_name.up()
                    return
      
                leaf = random.choice(LEAVES)
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=LEAF_STYLE)
                LEAVES.remove(leaf)

                nib_name.color('white')
                nib_name.back(length)

    # ----------------------------------------------------------------------------------------------------------------

    def asymmetric_tree_under127(self, nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
        if len(LEAVES) == 0:
            return
        nib_name.down()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.down()

            seq = self.get_seq()
            if start or next(seq) > 0.5:
                nib_name.pensize(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
                nib_name.left(angle)
                # asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
                nib_name.right(2 * angle)

                if len(LEAVES) == 0:
                    nib_name.up()
                    return

                leaf = random.choice(LEAVES)
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=LEAF_STYLE)
                LEAVES.remove(leaf)

                nib_name.color('white')
                nib_name.back(length)

    # ---------------------------------------------------------------------------------

    def asymmetric_tree_under600(self, nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
        if len(LEAVES) == 0:
            return
        nib_name.down()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.down()

            seq = self.get_seq()
            if start or next(seq) > 0.5:
                nib_name.pensize(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8, start)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8,start)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8, start)
                nib_name.left(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8, start)
                nib_name.right(2 * angle)

                if len(LEAVES) == 0:
                    nib_name.up()
                    return
  
                leaf = random.choice(LEAVES)
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=LEAF_STYLE)
                LEAVES.remove(leaf)
                nib_name.color('white')
                nib_name.back(length)

    def asym_roots(self, nib_name, ROOTS, length, levels, angle, root_palette, pensize):
        try:
            nib_name.color(random.choice(root_palette))
            if len(ROOTS) == 0:
                nib_name.up()
                return

            nib_name.down()
            nib_name.color(random.choice(root_palette))
            if levels == 0:

                if len(ROOTS) == 0:
                    return
                else:
                    root = random.choice(ROOTS)
                    nib_name.color(random.choice(root_palette))
                    nib_name.write(root, font=ROOT_STYLE, align="right")
                    ROOTS.remove(root)

            nib_name.color(random.choice(root_palette))
            if levels >= 1:
                nib_name.down()

                seq = self.get_seq()
                # if next(seq) > 0.5:
                if next(seq) > 0:
                    nib_name.pensize(pensize)
                    # nib_name.forward(length)
                    nib_name.right(angle)
                    nib_name.color(random.choice(root_palette))
                    self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4, True)
                    nib_name.right(angle)
                    self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4, True)
                    nib_name.left(3 * angle)
                    self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4, True)
                    nib_name.left(angle)
                    nib_name.color(random.choice(root_palette))
                    self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4, True)
                    nib_name.color(random.choice(root_palette))
                    nib_name.right(2 * angle)
                    if len(ROOTS) == 0:
                        nib_name.up()
                        return

                    nib_name.color(random.choice(root_palette))
                    nib_name.back(length)
        except object as e:
            print(e)

    @staticmethod
    def write_labels(nib_name, x, y, address):
        try:
# __pragma__ ('ecom')
            #?y = -y
# __pragma__ ('ecom')
            nib_name.goto(x, y)
            nib_name.write(address, font=LABEL_STYLE, align='left')
        except object as e:
            print(e)

# __pragma__ ('nokwargs')
