from turtle import Turtle
import random
import turtle
from nft_data import NFTData
import math
import tree_builders as tb


# Transcrypt random does not have randrange so we will monkeypatch a version of it
# __pragma__ ('ecom')
'''?
def randrange(start, end, step):
    rand = random.randint(start, end-1)
    return rand - rand%step + start

random.randrange = randrange
?'''
# __pragma__ ('noecom')


# Fall colour palettes------------------------------------------------------------------- #
# pallettes https://avemateiu.com/20-fall-color-palettes-2019/
AUTUMN_COLOURS1 = ['#D75915', '#D38E10', '#F7E0AC', '#C39367']  # yellow theme (LEAVES)
AUTUMN_COLOURS2 = ['#ff9136', '#9f1006', '#D23736', '#511a1f', '#380507']  # RED LEAVES
AUTUMN_COLOURS3 = ['#474c33', '#938a5d', '#e1bf86', '#bf642f', '#242c31']  # ROAD TRIP mix greens/orange pastel(ROOTS)
# https://looka.com/blog/12-fall-color-palettes/
AUTUMN_COLOURS4 = ['#F5B3B4', '#D15656', '#94353C', '#694364', '#B58BAB',
                   '#E3D1E2']  # red light to dark(3) + purple dark to light(3) (ROOTS)
AUTUMN_COLOURS5 = ['#391615', '#5e2d3b', '#92425f']  # DARK BROWN TO MAROON (ROOTS)
AUTUMN_COLOURS6 = ['#2f43b5', '#156870', '#016c8c', '#4ebfc7']  # turquoise blue (leaves)
AUTUMN_COLOURS7 = ['#4e4d49', '#725e45', '#b7946a', '#e2c58d', '#d6cfbf']  # ochre roots (light to dark)
SPRING_COLOURS = ['#27AA80', '#32FF6A', '#A8FF3E', '#F4FF61']  # GREEN (LEAVES)
PURPLE_PALETTE = ['#52057B', '#892CDC', '#BC6FF1', '#9D0191']
GOLD_PALETTE = ['#BD574E', '#F67E7D', '#FFAD87', '#843B62']  # root

LEAF_PALETTES = [AUTUMN_COLOURS1, AUTUMN_COLOURS2, AUTUMN_COLOURS6, SPRING_COLOURS, PURPLE_PALETTE]
ROOT_PALETTES = [AUTUMN_COLOURS3, AUTUMN_COLOURS4, AUTUMN_COLOURS5, AUTUMN_COLOURS7, GOLD_PALETTE]


# ----------------------------------------------------------------------------------------


# - Create Turtles --------
def create_turtles():
    def make_nib():
        nib = Turtle()
        nib.hideturtle()  # __:skip
        nib.up()
        nib.speed('fastest')
        nib.goto(0, -100)
        nib.shape('turtle')  # __:skip
        nib.color('white')
        nib.shape('triangle')  # __:skip
        return nib

    nib_names = ['trunk', 'root', 'tree1', 'tree2', 'snow']
    all_nibs = {nib: make_nib() for nib in nib_names}

    all_nibs['tree1'].left(90)
    all_nibs['tree2'].right(90)
    all_nibs['root'].right(90)
    all_nibs['trunk'].right(90)

    return all_nibs


def nft_draw(nft, screen=None):
    turtle.delay(0)  # __:skip
    turtle.tracer(0)  # __:skip

    nibs = create_turtles()

    palette = random.choice(LEAF_PALETTES)
    root_palette = random.choice(ROOT_PALETTES)

    # ---GLOBALS------
    LEAVES = [(nft.token_id_list[i][0:6]) for i in range(len(nft.token_id_list))]  # ['leaf' for i in range(19)]
    ROOTS = [(nft.from_address_list[i][0:4]) for i in range(len(nft.from_address_list))]  # ['roots' for i in range (19)]

    # total leaves needed = r to the pow(levels). Hence levels = log(leaves, base r)
    LEAVES_NEEDED = len(LEAVES)
    ROOTS_NEEDED = len(ROOTS)
    print(LEAVES_NEEDED, ROOTS_NEEDED)
    level_tree = 2 if LEAVES_NEEDED < 2 else round(math.log(LEAVES_NEEDED, 2))
    # level_root = 2 if ROOTS_NEEDED < 2 else round(math.log(ROOTS_NEEDED, 2))
    # ----------------------------------------------------------

    if LEAVES_NEEDED == 0:
        nibs['trunk'].goto(0, 0)
        nibs['trunk'].write("No ERC721 NFTs found. Try another wallet.", align='center')  # __:skip
        # __pragma__('js', '{}', 'window.alert("No ERC721 NFTs found. Try another wallet.")')

    elif LEAVES_NEEDED < 8:
        tb.multi_turtle_tree(palette, LEAVES, angle_step=15)
        tb.asym_roots(nib_name=nibs['root'], ROOTS=ROOTS,
                      length=random.randrange(70, 90, 10),
                      levels=3,
                      angle=(random.randrange(45, 55, 5)),
                      root_palette=root_palette,
                      pensize=6)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-195, address=nft.address[0:6])

    elif LEAVES_NEEDED < 15:
        angle_range = [random.randrange(-60, -30, 10), random.randrange(30, 60, 10)]
        tb.asymmetric_tree_under14(nib_name=nibs['tree1'],
                                   LEAVES=LEAVES,
                                   length=random.randrange(100, 140, 20),
                                   levels=random.randint(4, 5),
                                   angle=random.choice(angle_range),
                                   palette=palette, pensize=10)
        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(70, 90, 10),
                      levels=3,
                      angle=(random.randrange(45, 55, 5)),
                      root_palette=root_palette,
                      pensize=7)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-260, address=nft.address[0:6])

    elif LEAVES_NEEDED < 31:
        tb.asymmetric_tree_under47(nib_name=nibs['tree1'],
                                   LEAVES=LEAVES,
                                   length=random.randrange(140, 200, 20),
                                   levels=random.randint(4, 6),
                                   angle=random.randrange(-55, 55, 35),
                                   palette=palette,
                                   pensize=10)

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(70, 90, 10),
                      levels=3,
                      angle=(random.randrange(25, 40, 5)),
                      root_palette=root_palette,
                      pensize=7)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-260, address=nft.address[0:6])

    elif LEAVES_NEEDED < 48:
        functions_ = [
            (tb.sym_tree, (nibs['tree1'], LEAVES, 100, level_tree, random.randrange(10, 40, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under47,
             (nibs['tree1'], LEAVES, random.randrange(140, 200, 20), 5, random.randrange(-55, 55, 35), palette, 10))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(70, 90, 10),
                      levels=4,
                      angle=(random.randrange(25, 40, 5)),
                      root_palette=root_palette,
                      pensize=10)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-260, address=nft.address[0:6])

    elif LEAVES_NEEDED < 128:
        angle_range = [random.randrange(-40, -10, 5), random.randrange(10, 40, 5)]

        functions_ = [
            (tb.sym_tree, (nibs['tree1'], LEAVES, 130, level_tree, random.randrange(15, 45, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under127,
             (nibs['tree1'], LEAVES, random.randrange(120, 160, 20), 6, random.choice(angle_range), palette, 10))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(80, 110, 10),
                      levels=4,
                      angle=(random.randrange(25, 40, 5)),
                      root_palette=root_palette,
                      pensize=10)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-280, address=nft.address[0:6])

    elif LEAVES_NEEDED < 301:
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        functions_ = [
            (tb.sym_tree, (nibs['tree1'], LEAVES, 130, level_tree, random.randrange(20, 45, 5), palette, 10, 0.75)),
            (tb.asymmetric_tree_under600,
             (nibs['tree1'], LEAVES, random.randrange(120, 140, 20), random.randint(6, 8), random.choice(angle_range), palette, 10))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(80, 110, 10),
                      levels=4,
                      angle=(random.randrange(25, 40, 5)),
                      root_palette=root_palette,
                      pensize=10)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-280, address=nft.address[0:6])

    elif LEAVES_NEEDED < 701:
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        functions_ = [
            (tb.sym_tree, (nibs['tree1'], LEAVES, 120, level_tree, random.randrange(15, 55, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under600,
             (nibs['tree1'], LEAVES, random.randrange(130, 140, 10), random.randint(8, 9), random.choice(angle_range), palette, 10))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(110, 130, 10),
                      levels=4,
                      angle=(random.randrange(30, 40, 5)),
                      root_palette=root_palette,
                      pensize=10)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-280, address=nft.address[0:6])

    else:
        level_tree = level_tree - 1
        angle_range = [random.randrange(-40, -10, 10), random.randrange(10, 40, 10)]

        random.random()
        functions_ = [
            (tb.sym_tree, (nibs['tree1'], LEAVES, 120, level_tree, random.randrange(15, 45, 10), palette, 10, 0.8)),
            (tb.asymmetric_tree_under600, (
                nibs['tree1'], LEAVES, random.randrange(110, 130, 10), random.randint(9, 10), random.choice(angle_range), palette, 10))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=nibs['root'],
                      ROOTS=ROOTS,
                      length=random.randrange(80, 110, 10),
                      levels=5,
                      angle=(random.randrange(35, 40, 5)),
                      root_palette=root_palette,
                      pensize=10)

        tb.write_labels(nib_name=nibs['trunk'], x=-300, y=-280, address=nft.address[0:6])

    if screen:
        screen.mainloop()


# __pragma__ ('skip')
if __name__ == '__main__':
    import os
    from nft_data import ETHERSCAN_KEY

    try:
        os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
    except Exception as ex:
        print(ex)

    nftdata = NFTData()
    nftdata.get_data()

    from turtle import Screen
    scr = Screen()
    scr.setup(width=900, height=900)
    scr.bgcolor('black')

    nft_draw(nftdata, scr)
    # __pragma__ ('noskip')
