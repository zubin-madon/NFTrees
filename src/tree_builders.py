from turtle import Turtle
import random


# --- Tree Functions--------
class TreeBuilder:
    def __init__(self, seq):
        self.seq = seq

    def get_seq(self):
        for n in self.seq:
            yield n

    # --- pseudo "randomizer" functions based on predefined sequence
    def choose(self, seq, lst):
        return lst[int(next(seq) * len(lst))]

    def choose_int(self, seq, start, end):
        return self.choose(seq, range(start, end + 1))

    def choose_range(self, seq, start, end, step):
        rand = self.choose(seq, range(start, end))
        adj_rand = rand - (rand % step) + (start % step)
        return adj_rand

    def multi_turtle_tree(self, palette, LEAVES, angle_step):
        turtles_ = []
        for i in range(len(LEAVES)):
            tim = Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(0, -100)
            tim.left(90)
            tim.pencolor("white")
            turtles_.append(tim)
        for i in range(len(turtles_)):
            turtles_[i].pendown()
            turtles_[i].pensize(6)
            length1 = random.randrange(80, 180, 20)
            turtles_[i].forward(length1)
            angle1 = random.randrange(-55, 55, angle_step)
            turtles_[i].left(angle1)
            turtles_[i].pensize(3)
            length2 = length1 * 0.618
            turtles_[i].forward(length2)

            if random.random() <= 0.618:
                # random.seed()
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
                    turtles_[i].pencolor(random.choice(palette))
                    leaf = random.choice(LEAVES)
                    turtles_[i].write(leaf)
                    LEAVES.remove(leaf)
                    turtles_[i].pencolor('white')

                else:
                    if len(LEAVES) == 0:
                        pass
                    else:
                        turtles_[i].pencolor(random.choice(palette))
                        leaf = random.choice(LEAVES)
                        turtles_[i].write(leaf)
                        LEAVES.remove(leaf)
                        turtles_[i].pencolor('white')

            else:
                if len(LEAVES) == 0:
                    pass
                else:
                    random.seed(50)
                    turtles_[i].pencolor(random.choice(palette))
                    leaf = random.choice(LEAVES)
                    turtles_[i].write(leaf)
                    LEAVES.remove(leaf)
                    turtles_[i].pencolor('white')
                    return

    # ----------Symmetrical Tree--------------------------------------

    def sym_tree(self, nib_name, length, levels, angle, len_reduce, palette, LEAVES, pen_size):
        if len(LEAVES) == 0:
            nib_name.penup()
            return

        nib_name.pendown()
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
            style = ('RootBeer', 10, 'bold')
            nib_name.pencolor(random.choice(palette))
            nib_name.write(leaf, font=style)
            nib_name.pencolor('white')
            LEAVES.remove(leaf)

        nib_name.backward(length)

    # -------------ASYMMETRIC TREE FUNCTION--------------------

    def asymmetric_tree_under14(self, nib_name, LEAVES, length, levels, angle, palette, pensize):
        if len(LEAVES) == 0:
            return
        nib_name.pendown()
        if levels == 0:
            return

        if levels >= 1:
            nib_name.pendown()

            seq = self.get_seq()
            if next(seq) > 0.5:
                nib_name.width(pensize)
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
                    nib_name.penup()
                    return
                else:
                    leaf = random.choice(LEAVES)
                    style = ('RootBeer', 10, 'bold')
                    nib_name.pencolor(random.choice(palette))
                    nib_name.write(leaf, font=style)
                    LEAVES.remove(leaf)
                    nib_name.pencolor('white')

                nib_name.color('white')
                nib_name.backward(length)

    # -------------------------------------------------------------------------------------------------------------------

    def asymmetric_tree_under47(self, nib_name, LEAVES, length, levels, angle, palette, pensize):
        if len(LEAVES) == 0:
            return
        nib_name.pendown()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.pendown()
            seq = self.get_seq()
            if next(seq) > 0.5:
                nib_name.width(pensize)
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
                    nib_name.penup()
                    return
                else:
                    leaf = random.choice(LEAVES)
                    style = ('RootBeer', 10, 'bold')
                    nib_name.pencolor(random.choice(palette))
                    nib_name.write(leaf, font=style)
                    LEAVES.remove(leaf)
                    nib_name.pencolor('white')

                nib_name.color('white')
                nib_name.backward(length)

    # ----------------------------------------------------------------------------------------------------------------

    def asymmetric_tree_under127(self, nib_name, LEAVES, length, levels, angle, palette, pensize):
        if len(LEAVES) == 0:
            return
        nib_name.pendown()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.pendown()

            seq = self.get_seq()
            if next(seq) > 0.5:
                nib_name.width(pensize)
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
                    nib_name.penup()
                    return
                else:
                    leaf = random.choice(LEAVES)
                    style = ('RootBeer', 10, 'bold')
                    nib_name.pencolor(random.choice(palette))
                    nib_name.write(leaf, font=style)
                    LEAVES.remove(leaf)
                    nib_name.pencolor('white')

                nib_name.color('white')
                nib_name.backward(length)

    # ---------------------------------------------------------------------------------

    def asymmetric_tree_under600(self, nib_name, LEAVES, length, levels, angle, palette, pensize):
        if len(LEAVES) == 0:
            return
        nib_name.pendown()
        if levels == 0:
            return
        if levels >= 1:
            nib_name.pendown()

            seq = self.get_seq()
            if next(seq) > 0.5:
                nib_name.width(pensize)
                nib_name.color('white')
                nib_name.forward(length)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
                nib_name.left(angle)
                self.asymmetric_tree_under127(nib_name, LEAVES, length * 0.8, levels - 1, angle, palette, pensize * 0.8)
                nib_name.right(2 * angle)

                if len(LEAVES) == 0:
                    nib_name.penup()
                    return
                else:
                    leaf = random.choice(LEAVES)
                    style = ('RootBeer', 10, 'bold')
                    nib_name.pencolor(random.choice(palette))
                    nib_name.write(leaf, font=style)
                    LEAVES.remove(leaf)
                    nib_name.pencolor('white')

                nib_name.color('white')
                nib_name.backward(length)

    def asym_roots(self, nib_name, ROOTS, length, levels, angle, root_palette, pensize):
        nib_name.color(random.choice(root_palette))
        if len(ROOTS) == 0:
            nib_name.penup()
            return

        nib_name.pendown()
        nib_name.color(random.choice(root_palette))
        nib_name.pencolor(random.choice(root_palette))
        if levels == 0:

            if len(ROOTS) == 0:
                return
            else:
                root = random.choice(ROOTS)
                style = ('RootBeer', 10, 'bold')
                nib_name.pencolor(random.choice(root_palette))
                nib_name.write(root, font=style, align="right")
                ROOTS.remove(root)

        nib_name.color(random.choice(root_palette))
        nib_name.pencolor(random.choice(root_palette))
        if levels >= 1:
            nib_name.pendown()

            seq = self.get_seq()
            if next(seq) > 0.5:
                nib_name.width(pensize)
                # nib_name.forward(length)
                nib_name.right(angle)
                nib_name.pencolor(random.choice(root_palette))
                self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.right(angle)
                self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.left(3 * angle)
                self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.left(angle)
                nib_name.color(random.choice(root_palette))
                self.asymmetric_tree_under127(nib_name, ROOTS, length * 0.9, levels - 1, angle * 0.3, root_palette, pensize * 0.4)
                nib_name.color(random.choice(root_palette))
                nib_name.right(2 * angle)
                if len(ROOTS) == 0:
                    nib_name.penup()
                    return
                nib_name.color(random.choice(root_palette))
                nib_name.backward(length)

    @staticmethod
    def write_labels(nib_name, x, y, address):
        style = ('RootBeer', 14, 'bold')
        nib_name.goto(x, y)
        nib_name.write(address, align='left', font=style)
