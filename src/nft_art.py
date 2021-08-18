from turtle import Screen, Turtle
import random
import turtle
import math
from datetime import date, datetime

from nft_data import NFTData
import tree_builders as tb


# Fall colour palettes------------------------------------------------------------------- #
# pallettes https://avemateiu.com/20-fall-color-palettes-2019/
AUTUMN_COLOURS1 = ['#D75915', '#D38E10', '#F7E0AC', '#C39367']  # yellow theme (LEAVES)
AUTUMN_COLOURS2 = ['#ff9136', '#9f1006', '#D23736', '#511a1f', '#380507']  # RED LEAVES
AUTUMN_COLOURS3 = ['#474c33', '#938a5d', '#e1bf86', '#bf642f',
                   '#242c31']  # ROAD TRIP mix greens/orange pastel(ROOTS)
# https://looka.com/blog/12-fall-color-palettes/
AUTUMN_COLOURS4 = ['#F5B3B4', '#D15656', '#94353C', '#694364', '#B58BAB',
                   '#E3D1E2']  # red light to dark(3) + purple dark to light(3) (ROOTS)
AUTUMN_COLOURS5 = ['#391615', '#5e2d3b', '#92425f']  # DARK BROWN TO MAROON (ROOTS)
AUTUMN_COLOURS6 = ['#2f43b5', '#156870', '#016c8c', '#4ebfc7']  # turquoise blue (leaves)
AUTUMN_COLOURS7 = ['#4e4d49', '#725e45', '#b7946a', '#e2c58d', '#d6cfbf']  # ochre roots (light to dark)
SPRING_COLOURS = ['#27AA80', '#32FF6A', '#A8FF3E', '#F4FF61']  # GREEN (LEAVES)
PURPLE_PALETTE = ['#52057B', '#892CDC', '#BC6FF1', '#9D0191']
GOLD_PALETTE = ['#BD574E', '#F67E7D', '#FFAD87', '#843B62'] #root

LEAF_PALETTES = [AUTUMN_COLOURS1, AUTUMN_COLOURS2, AUTUMN_COLOURS6, SPRING_COLOURS, PURPLE_PALETTE]
ROOT_PALETTES = [AUTUMN_COLOURS3, AUTUMN_COLOURS4, AUTUMN_COLOURS5, AUTUMN_COLOURS7, GOLD_PALETTE]
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------

def nft_draw(nft, tree_seed=None):
    # - Create Turtles --------
    all_nibs = []
    for i in range(5):
        nib = Turtle()
        nib.hideturtle()
        nib.penup()
        nib.speed('fastest')
        nib.goto(0, -100)
        nib.shape('turtle')
        nib.pencolor('white')
        nib.shape('triangle')
        all_nibs.append(nib)
    # ---Name the Turtles------------------
    trunk = all_nibs[0]
    root = all_nibs[1]
    tree_one = all_nibs[2]
    tree_two = all_nibs[3]
    snow = all_nibs[4]
    # ---Orient the turtles and send them to their places
    tree_one.left(90)
    tree_two.right(90)
    root.right(90)
    trunk.right(90)
    turtle.tracer(0)
    turtle.delay(0)


    # ---GLOBALS------
    LEAVES = [(nft.token_id_list[i][0:6]) for i in range(len(nft.token_id_list))]  # ['leaf' for i in range(19)]
    ROOTS = [(nft.from_address_list[i][0:4]) for i in range(len(nft.from_address_list))]  # ['roots' for i in range (19)]

    # total leaves needed = r to the pow(levels). Hence levels = log(leaves, base r)
    LEAVES_NEEDED = len(LEAVES)
    ROOTS_NEEDED = len(ROOTS)
    print(LEAVES_NEEDED, ROOTS_NEEDED)
    level_tree = 2 if LEAVES_NEEDED == 0 or LEAVES_NEEDED == 1 else round(math.log(LEAVES_NEEDED, 2))
    level_root = 2 if ROOTS_NEEDED == 0 or ROOTS_NEEDED == 1 else round(math.log(ROOTS_NEEDED, 2))

    palette = random.choice(LEAF_PALETTES)
    root_palette = random.choice(ROOT_PALETTES)

    if LEAVES_NEEDED == 0:
        trunk.goto(0, 0)
        trunk.write("No ERC721 NFTs found. Try another wallet.", align = 'center')

    if LEAVES_NEEDED <= 7:
        tb.multi_turtle_tree(palette, LEAVES, angle_step=15)
        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(70, 90, 10), levels=3,
                                 angle=(random.randrange(45, 55, 5)), root_palette=root_palette,
                                 pensize=6)

        tb.write_labels(nib_name=trunk, x=-300, y= -195, address=nft.address[0:6])

    if 8 <= LEAVES_NEEDED <= 14:
        angle_range = [random.randrange(-60, -30, 10), random.randrange(30, 60, 10)]
        tb.asymmetric_tree_under14(nib_name=tree_one, LEAVES=LEAVES, length=random.randrange(100,140,20),
                                              levels=random.randint(4,5), angle=random.choice(angle_range),
                                              palette=palette, pensize=10)
        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(70, 90, 10), levels=3,
                                 angle=(random.randrange(45, 55, 5)), root_palette=root_palette,
                                 pensize=7)

        tb.write_labels(nib_name=trunk, x=-300, y=-260, address=nft.address[0:6])

    if 15 <= LEAVES_NEEDED <= 30:
        tb.asymmetric_tree_under47(nib_name=tree_one, LEAVES=LEAVES, length=random.randrange(140, 200, 20),
                                              levels=random.randint(4,6), angle=random.randrange(-55, 55, 35),
                                              palette=palette, pensize=10)

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(70, 90, 10), levels=3,
                                 angle=(random.randrange(25, 40, 5)), root_palette=root_palette,
                                 pensize=7)

        tb.write_labels(nib_name=trunk, x=-300, y=-260, address=nft.address[0:6])

    if 31 <= LEAVES_NEEDED <= 47:
        functions_ = [(tb.sym_tree,(tree_one, 100, level_tree, random.randrange(10, 40, 10),
                                   0.75, palette, LEAVES, 10)),
        (tb.asymmetric_tree_under47, ((tree_one, LEAVES,
                                                  random.randrange(140, 200, 20),
                                                  5, random.randrange(-55, 55, 35),
                                                  palette, 10)))]

        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(70, 90, 10), levels=4,
                                 angle=(random.randrange(25, 40, 5)), root_palette=root_palette,
                                 pensize=10)

        tb.write_labels(nib_name=trunk, x=-300, y=-260, address=nft.address[0:6])

    if 48 <= LEAVES_NEEDED <= 127:
        angle_range = [random.randrange(-40, -10, 5), random.randrange(10, 40, 5)]

        functions_ = [(tb.sym_tree, (tree_one, 130, level_tree, random.randrange(15, 45, 10),
                               0.75, palette, LEAVES, 10)), (tb.asymmetric_tree_under127, (tree_one, LEAVES, random.randrange(120, 160, 20),
                                               6, random.choice(angle_range),
                                               palette, 10))]
        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(80, 110, 10), levels=4,
                                 angle=(random.randrange(25, 40, 5)), root_palette=root_palette,
                                 pensize=10)

        tb.write_labels(nib_name=trunk, x=-300, y=-280, address=nft.address[0:6])

    if 128 <= LEAVES_NEEDED <= 300:
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        functions_ = [
            (tb.sym_tree, (tree_one, 130, level_tree, random.randrange(20, 45, 5), 0.75, palette, LEAVES, 10)),
            (tb.asymmetric_tree_under600, (tree_one, LEAVES, random.randrange(120, 140, 20), random.randint(6,8),
                                                      random.choice(angle_range), palette, 10))
        ]
        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(80, 110, 10), levels=4,
                                 angle=(random.randrange(25, 40, 5)), root_palette=root_palette,
                                 pensize=10)

        tb.write_labels(nib_name=trunk, x=-300, y=-280, address=nft.address[0:6])

    if 301 <= LEAVES_NEEDED <= 700:
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        functions_ = [
            (tb.sym_tree,
             (tree_one, 120, level_tree, random.randrange(15, 55, 10), 0.75, palette, LEAVES, 10)),
            (tb.asymmetric_tree_under600,
             (tree_one, LEAVES, random.randrange(130, 140, 10), random.randint(8, 9),
              random.choice(angle_range), palette, 10))
        ]
        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(110, 130, 10), levels=4,
                                 angle=(random.randrange(30, 40, 5)), root_palette=root_palette, pensize=10)

        tb.write_labels(nib_name=trunk, x=-300, y=-280, address=nft.address[0:6])

    if 701 <= LEAVES_NEEDED:
        level_tree = level_tree - 1
        angle_range = [random.randrange(-40, -10, 10), random.randrange(10, 40, 10)]

        #tb.root_function(nib_name=root, ROOTS=ROOTS, length=80, levels=level_root-4, angle=35,
                                    # root_palette=root_palette, pensize=10)


        random.random()
        functions_ = [
            (tb.sym_tree,
             (tree_one, 120, level_tree, random.randrange(15, 45, 10), 0.8, palette, LEAVES, 10)),
            (tb.asymmetric_tree_under600,
             (tree_one, LEAVES, random.randrange(110, 130, 10), random.randint(9, 10),
              random.choice(angle_range), palette, 10))
        ]
        x = random.choice(functions_)
        x[0](*x[1])

        tb.asym_roots(nib_name=root, ROOTS=ROOTS, length=random.randrange(80, 110, 10), levels=5,
                                 angle=(random.randrange(35, 40, 5)), root_palette=root_palette, pensize=10)

        tb.write_labels(nib_name=trunk, x=-300, y=-280, address=nft.address[0:6])



# __pragma__ ('skip')
if __name__ == '__main__':
    import os
    import time
    from nft_data import ETHERSCAN_KEY

    try:
        os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
    except Exception as ex:
        print(ex)

    from turtle import Screen

    screen = Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor('black')

    TEST_ALL = True
    if TEST_ALL:
        from nft_data import test_data

        for wallet_id in test_data.values():
            screen.reset()
            nftdata = NFTData(wallet_id)
            nftdata.get_data()
            nft_draw(nftdata)
            screen.update()
            time.sleep(10)
    else:
        nftdata = NFTData()
        nftdata.get_data()
        # nft_draw(nftdata, 1629084036295)
        nft_draw(nftdata)
        screen.mainloop()
# __pragma__ ('noskip')
