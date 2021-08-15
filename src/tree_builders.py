from turtle import Turtle
import random
import time


# --- Tree Functions--------

def multi_turtle_tree(palette, LEAVES, angle_step):
    turtles_ = []

    for i in range(len(LEAVES)):
        tim = Turtle()
        tim.hideturtle()
        tim.up()
        tim.goto(0, -100)
        tim.left(90)
        tim.color("white")
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
    else:
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
            style = ('RootBeer', 10, 'bold')
            nib_name.color(random.choice(palette))
            nib_name.write(leaf, font=style)
            nib_name.color('white')
            LEAVES.remove(leaf)

            nib_name.backward(length)


# -------------ASYMMETRIC TREE FUNCTION--------------------
def asymmetric_tree_under14(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) > 0:
        nib_name.down()
        if levels > 0:
            nib_name.down()
            random.seed(46)
            if random.random() > 0.5:
                nib_name.width(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.right(angle)
                nib_name.left(3 * angle)
                asymmetric_tree_under14(nib_name, LEAVES, length * 0.618, levels - 1, angle, palette, pensize * 0.5)
                nib_name.left(angle)
                nib_name.right(2 * angle)
                random.seed(int(time.time() * 1000))
                if len(LEAVES) == 0:
                    nib_name.up()
                else:
                    leaf = random.choice(LEAVES)
                    style = ('RootBeer', 10, 'bold')
                    nib_name.color(random.choice(palette))
                    nib_name.write(leaf, font=style)
                    LEAVES.remove(leaf)
                    nib_name.color('white')

                    random.seed(46)
                    nib_name.color('white')
                    nib_name.backward(length)


# -------------------------------------------------------------------------------------------------------------------
def asymmetric_tree_under47(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels > 0:
        nib_name.down()
        random.seed(46)
        if random.random() > 0.5:
            nib_name.width(pensize)
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

            random.seed(int(time.time() * 1000))
            if len(LEAVES) == 0:
                nib_name.up()
            else:
                leaf = random.choice(LEAVES)
                style = ('RootBeer', 10, 'bold')
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=style)
                LEAVES.remove(leaf)
                nib_name.color('white')

                random.seed(46)
                nib_name.color('white')
                nib_name.backward(length)


# ----------------------------------------------------------------------------------------------------------------
def asymmetric_tree_under127(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) == 0:
        return

    nib_name.down()
    if levels > 0:
        nib_name.down()
        random.seed(46)
        if random.random() > 0.5:
            nib_name.width(pensize)
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
            random.seed(int(time.time() * 1000))
            if len(LEAVES) == 0:
                nib_name.up()
                return
            else:
                leaf = random.choice(LEAVES)
                style = ('RootBeer', 10, 'bold')
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=style)
                LEAVES.remove(leaf)
                nib_name.color('white')
            random.seed(46)
            nib_name.color('white')
            nib_name.backward(length)


# ---------------------------------------------------------------------------------
def asymmetric_tree_under600(nib_name, LEAVES, length, levels, angle, palette, pensize):
    if len(LEAVES) == 0:
        return
    nib_name.down()
    if levels == 0:
        return
    if levels >= 1:
        nib_name.down()
        random.seed(46)
        if random.random() > 0.5:
            nib_name.width(pensize)
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
            random.seed(int(time.time() * 1000))
            if len(LEAVES) == 0:
                nib_name.up()
                return
            else:
                leaf = random.choice(LEAVES)
                style = ('RootBeer', 10, 'bold')
                nib_name.color(random.choice(palette))
                nib_name.write(leaf, font=style)
                LEAVES.remove(leaf)
                nib_name.color('white')
            random.seed(46)
            nib_name.color('white')
            nib_name.backward(length)


def asym_roots(nib_name, ROOTS, length, levels, angle, root_palette, pensize):
    def get_color(root_color):
        return random.choice(root_color)

    nib_name.color(get_color(root_palette))
    if len(ROOTS) == 0:
        nib_name.up()
    else:
        nib_name.down()
        nib_name.color(get_color(root_palette))
        nib_name.color(get_color(root_palette))
        if levels == 0:
            random.seed(int(time.time() * 1000))
            if len(ROOTS) == 0:
                return
            else:
                root = random.choice(ROOTS)
                style = ('RootBeer', 10, 'bold')
                nib_name.color(random.choice(root_palette))
                nib_name.write(root, font=style, align="right")
                ROOTS.remove(root)

        random.seed(46)
        nib_name.color(get_color(root_palette))
        nib_name.color(get_color(root_palette))

        if levels > 0:
            nib_name.down()
            random.seed(46)
            if random.random() > 0.5:
                nib_name.width(pensize)
                nib_name.right(angle)
                nib_name.color(get_color(root_palette))
                asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.right(angle)
                asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.left(3 * angle)
                asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.left(angle)
                nib_name.color(get_color(root_palette))
                asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.color(get_color(root_palette))
                nib_name.right(2 * angle)

                if len(ROOTS) == 0:
                    nib_name.up()
                else:
                    nib_name.color(get_color(root_palette))
                    nib_name.backward(length)


def write_labels(nib_name, x, y, address):
    style = ('RootBeer', 14, 'bold')
    nib_name.goto(x, y)
    nib_name.write(address, align='left', font = style)
