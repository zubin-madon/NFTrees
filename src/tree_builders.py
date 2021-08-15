from turtle import Turtle
import random
import time


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


# --- Tree Functions--------
# __pragma__ ('kwargs')
def multi_turtle_tree(palette, LEAVES, angle_step):
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

        random.seed(50)
        if random.random() <= 0.618:
            random.seed(int(time.time() * 1000))
            turtles_[i].pensize(2)
            if angle1 < 0:
                angle2 = random.randrange(-42, -7, 14)
                turtles_[i].left(angle2)
            if angle1 > 0:
                angle2 = random.randrange(7, 42, 14)
                turtles_[i].left(angle2)
            turtles_[i].forward(0.618 * length2)
            random.seed(random.randint(0, 100))
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
                if len(LEAVES) > 0:
                    turtles_[i].color(random.choice(palette))
                    leaf = random.choice(LEAVES)
                    turtles_[i].write(leaf)
                    LEAVES.remove(leaf)
                    turtles_[i].color('white')
        else:
            if len(LEAVES) > 0:
                turtles_[i].color(random.choice(palette))
                leaf = random.choice(LEAVES)
                turtles_[i].write(leaf)
                LEAVES.remove(leaf)
                turtles_[i].color('white')


# ----------Symmetrical Tree--------------------------------------
def sym_tree(nib_name, LEAVES, length, levels, angle, palette, pen_size, len_reduce):
    if len(LEAVES) == 0:
        nib_name.up()
        return

    nib_name.down()
    if levels > 0:
        nib_name.pensize(pen_size)
        nib_name.forward(length)
        nib_name.right(angle)
        sym_tree(nib_name, LEAVES, length * len_reduce, levels - 1, angle, palette, pen_size * 0.6, len_reduce)
        nib_name.left(angle * 2)
        sym_tree(nib_name, LEAVES, length * len_reduce, levels - 1, angle, palette, pen_size * 0.6, len_reduce)
        nib_name.right(angle)

        leaf = random.choice(LEAVES)
        nib_name.color(random.choice(palette))
        nib_name.write(leaf, font=LEAF_STYLE)
        nib_name.color('white')
        LEAVES.remove(leaf)

        nib_name.back(length)


# -------------ASYMMETRIC TREE FUNCTION--------------------
def asymmetric_tree_under14(nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels > 0:
        nib_name.down()

        # TODO: Factor in starting levels or # of leaves to insure there is *something* generated in the 1st few rounds
        if start or random.random() > 0.2:
            nib_name.pensize(pensize)
            nib_name.color('white')
            nib_name.forward(length)
            nib_name.right(angle)
            asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
            nib_name.right(angle)
            nib_name.left(3 * angle)
            asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
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
def asymmetric_tree_under47(nib_name, LEAVES, length, levels, angle, palette, pensize, start=False):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels > 0:
        nib_name.down()
        # TODO: Factor in starting levels or # of leaves to insure there is *something* generated in the 1st few rounds
        if start or random.random() > 0.2:
            nib_name.pensize(pensize)
            nib_name.color('white')
            nib_name.forward(length)
            nib_name.right(angle)
            asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
            nib_name.right(angle)
            asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
            nib_name.left(3 * angle)
            asymmetric_tree_under47(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
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
def asymmetric_tree_under127(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels > 0:
        nib_name.down()

        # TODO: Factor in starting levels or # of leaves to insure there is *something* generated in the 1st few rounds
        if random.random() > 0.2:  # Cut off % for asymmetry
            nib_name.pensize(pensize)
            nib_name.color('white')
            nib_name.forward(length)
            nib_name.right(angle)
            asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
            nib_name.right(angle)
            asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
            nib_name.left(3 * angle)
            asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.6)
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


# ---------------------------------------------------------------------------------
def asymmetric_tree_under600(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels == 0:
        return

    nib_name.down()

    nib_name.pensize(pensize)
    nib_name.color('white')
    nib_name.forward(length)
    nib_name.right(angle)
    asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
    nib_name.right(angle)
    asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
    nib_name.left(3 * angle)
    asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
    nib_name.left(angle)
    asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
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


def asym_roots(nib_name, ROOTS, length, levels, angle, root_palette, pensize):
    print('aroot', nib_name, len(ROOTS), length, levels, angle, root_palette, pensize)
    
    def change_color(nib):
        nib.color(random.choice(root_palette))
        
    try:
        if len(ROOTS) == 0:
            nib_name.up()
            return

        nib_name.down()
        if levels == 0:
            root = random.choice(ROOTS)
            change_color(nib_name)
            nib_name.write(root, font=ROOT_STYLE, align="right")
            ROOTS.remove(root)
        else:
            change_color(nib_name)
            nib_name.down()

            nib_name.pensize(pensize)
            nib_name.right(angle)
            change_color(nib_name)
            asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
            nib_name.right(angle)
            asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
            nib_name.left(3 * angle)
            asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
            nib_name.left(angle)
            change_color(nib_name)
            asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
            change_color(nib_name)
            nib_name.right(2 * angle)

            if len(ROOTS) == 0:
                nib_name.up()
            else:
                print("ROOTS LEFT:", len(ROOTS))
                change_color(nib_name)
                nib_name.back(length)

    except object as e:
        print(e)


def write_labels(nib_name, x, y, address):
    try:
        nib_name.goto(x, y)
        nib_name.write(address, align='left', font=LABEL_STYLE)
    except object as e:
        print(e)

# __pragma__ ('nokwargs')
