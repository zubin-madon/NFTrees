import time
import random
import math

from nft_data import NFTData
import tree_builders as tb

USE_SVG = True

if USE_SVG:
    from turtle_svg import Turtle
    import turtle_svg as turtle
else:
    from turtle import Turtle
    import turtle

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
# __pragma__ ('kwargs')
# __pragma__ ('ecom')

'''?
from turtle import _svg
from turtle import _ns
from turtle import _offset

turtle._text = []

def turtle_reset_text():
    for text in turtle._text:
        _svg.removeChild (text)
        turtle._text = []
    
turtle.reset_text = turtle_reset_text


def turtle_write(self, txt, font=None, align='center'):
    if not font:
        font = ('RootBeer', 14, 'bold')
    text = document.createElementNS(_ns, 'text')
    text.setAttribute ('x', self.pos()[0] + _offset[0])
    text.setAttribute ('y', self.pos()[1] + _offset[1])
    text.setAttribute ('fill', self._pencolor)
    text.setAttribute ('align', align)
    text.setAttribute ('style', f'font-size:{font[1]*1.5}px; font-weight:{font[2]}; font-family:{font[0]}, sans-serif;')
    text.innerHTML = txt
    _svg.appendChild(text)
    turtle._text.append (text)
?'''
# __pragma__ ('noecom')
# __pragma__ ('nokwargs')

# pallettes https://avemateiu.com/20-fall-color-palettes-2019/
LEAF_PALETTES = {
    'AutumnAurora': ['#D75915', '#D38E10', '#F7E0AC', '#C39367'], 'RedSunset': ['#ff9136', '#9f1006', '#D23736', '#511a1f'],
    'GreenCauldron': ['#286140', '#67B080', '#AFCCB6', '#5DA1A3', '#696089'], 'Halloween': ['#C64820', '#CEBCC6', '#dbb0a2', '#653269'],
    'Turquoise': ['#2f43b5', '#156870', '#016c8c', '#4ebfc7'],
    'Gourd': ['#b52604', '#e24a07', '#ff9136', '#0c4052', '#125066'],
    'Lush': ['#27AA80', '#32FF6A', '#A8FF3E', '#F4FF61'],
    'PurpleHaze': ['#52057B', '#892CDC', '#BC6FF1', '#9D0191'],
    'MulledWine': ['#163763', '#eec73f', '#d63e16', '#600248'],
    'PinkSurprise': ['#9d6079', '#fa5770', '#ffa5b9', '#f0d9ea'],
    'Psychedellic': ['#133072', '#d5e6f7', '#d5adfb', '#f90052'],
    'Breezy': ['#FAC605', '#C1FFD7', '#B5DEFF', '#CAB8FF'],
    'WarmSummer': ['#D83A56', '#FF616D', '#FFEAC9', '#66DE93'],
    'SummerHue': ['#FF9292', '#FFB4B4', '#F1D1D0', '#E4BAD4'],
    'NeonMix': ['#FFD300', '#DE38C8', '#652EC7', '#B20346'],
    'LateSummer': ['#CA3422', '#FFA010', '#00AA13', '#578194'],
    'BlueRain': ['#234d74', '#355e84', '#6c92ab', '#c8d7e6'],
    'PumpkinSpice': ['#994900', '#c45400', '#d17200', '#f2e3d6'],
    'Retro': ['#FC95CA', '#FE1C80','#ff5f01', '#ce0000'],
    'Prism': ['#ffff66', '#fc6e22', '#ff1493', '#c24cf6'],
    'Ferns': ['#FDC7D7', '#FF9DE6', '#A5D8F3', '#E8E500']
}
ROOT_PALETTES = {
    'DiffusedNeon': ['#CE96FB', '#FF8FCF', '#00C2BA', '#037A90'],
    'EarthyPastel': ['#B3ABA2', '#C7C1B9', '#A99D8C', '#7E6C59'],
    'OldForest': ['#D4B29D', '#B69885', '#928D8D', '#66636B'],
    'NeutralSoil': ['#945F3D', '#D7AD8C', '#E3DECA', '#999A98'],
    'AutumnHarvest': ['#5e2d3b', '#92425f', '#eaddd0', '#d2c1b0'],
    'Fall': ['#474c33', '#938a5d', '#e1bf86', '#bf642f', '#242c31'],
    'Merlot': ['#F5B3B4', '#D15656', '#94353C', '#694364', '#B58BAB', '#E3D1E2'],
    'Oakwood': ['#391615', '#5e2d3b', '#92425f', '#70052C'],
    'Ochre': ['#4e4d49', '#725e45', '#b7946a', '#e2c58d', '#d6cfbf'],
    'PumpkinSpice': ['#994900', '#c45400', '#d17200', '#f2e3d6'],
    'GoldenCorn': ['#BD574E', '#F67E7D', '#FFAD87', '#843B62'],
    'Tranquility': ['#d5ddef', '#bcb8ce', '#917898', '#4c394f'],
    'Eclipse': ['#FF560B', '#ED2D05', '#9C1304', '#6E0A05'],
    'Winter': ['#3D2C8D', '#916BBF', '#C996CC', '#6E3CBC'],
    'SpaceShift': ['#3B185F', '#A12568', '#B24080', '#FEC260'],
    'BlueLagoon': ['#001E6C', '#0F52BA', '#035397', '#5089C6'],
    'BlueRain': ['#234d74', '#355e84', '#6c92ab', '#c8d7e6']
}

variant = random.randint(1, 2)

level_range = 0
angle_range = 0
final_angle = 0
# ----------------------------------------------------------------------------------------


# - Create Turtles --------
def create_turtles():
    def make_nib():
        nib = Turtle()
        nib.hideturtle()  # __:skip
        nib.up()
        nib.speed('fastest')
        nib.goto(0, -100)  # __:skip
        nib.shape('turtle')  # __:skip
        nib.color('white')
        nib.shape('triangle')  # __:skip
        # __pragma__ ('ecom')
        '''?
        nib.goto(0, 100)
        def write(txt, kwargs):
            turtle_write(nib, txt, kwargs)
        
        nib.write = write
        
        # Turtle method aliases
        nib.pencolor = nib.color
        nib.penup = nib.up
        nib.pendown = nib.down
        nib.width = nib.pensize
        nib.backward = nib.back
        ?'''
        # __pragma__ ('noecom')

        return nib

    nib_names = ['trunk', 'root', 'tree']
    all_nibs = {nib: make_nib() for nib in nib_names}

    all_nibs['tree'].left(90)
    all_nibs['root'].right(90)
    all_nibs['trunk'].right(90)

    return all_nibs


def nft_draw(nft, tree_seed=None):
    nft.get_data()
    print(nft.block)
    global level_range, angle_range, final_angle
    turtle.delay(0)  # __:skip
    turtle.tracer(0)  # __:skip

    if tree_seed:
        random.seed(tree_seed)
    else:
        new_seed = int(time.time() * 1000)
        random.seed(new_seed)
        print("seed:", new_seed)  # __:skip

        # __pragma__ ('ecom')
        '''?
        if document.getElementById("mintBtn").disabled:
            print(f'?seed={new_seed}')
        ?'''

    # ?turtle.reset_text()
    # __pragma__ ('noecom')
    turtle.reset()
    turtle.bgcolor("black")

    nibs = create_turtles()

    leaf_palette_name = random.choice(list(LEAF_PALETTES.keys()))
    palette = LEAF_PALETTES[leaf_palette_name]
    root_palette_name = random.choice(list(ROOT_PALETTES.keys()))
    root_palette = ROOT_PALETTES[root_palette_name]

    # ---GLOBALS------
    LEAVES = [(nft.token_id_list[i][0:6]) for i in range(len(nft.token_id_list))]
    ROOTS = [(nft.from_address_list[i][0:4]) for i in range(len(nft.from_address_list))]

    # total leaves needed = r to the pow(levels). Hence levels = log(leaves, base r)
    LEAVES_NEEDED = len(LEAVES)
    ROOTS_NEEDED = len(ROOTS)
    level_tree = 2 if LEAVES_NEEDED < 2 else round(math.log(LEAVES_NEEDED, 2))
    # ----------------------------------------------------------
    print(LEAVES_NEEDED)
    if LEAVES_NEEDED == 0:
        nibs['trunk'].goto(0, 0)
        nibs['trunk'].write("No ERC721 NFTs found. Try another wallet.", align='center')

    elif LEAVES_NEEDED < 8:
        tb.multi_turtle_tree(palette, LEAVES, angle_step=15)

    elif LEAVES_NEEDED < 15:
        angle_range = [random.randrange(-60, -30, 10), random.randrange(30, 60, 10)]
        final_angle = random.choice(angle_range)
        tb.asymmetric_tree_under14(nib_name=nibs['tree'],
                                   LEAVES=LEAVES,
                                   length=random.randrange(100, 140, 20),
                                   levels=5,
                                   angle=final_angle,
                                   palette=palette, pensize=10)

    elif LEAVES_NEEDED < 31:
        tb.asymmetric_tree_under47(nib_name=nibs['tree'],
                                   LEAVES=LEAVES,
                                   length=random.randrange(140, 200, 20),
                                   levels=random.randint(4, 6),
                                   angle=random.randrange(-55, 55, 35),
                                   palette=palette,
                                   pensize=10,
                                   start=True)

    elif LEAVES_NEEDED < 48:

        functions_ = [
            (tb.sym_tree, (nibs['tree'], LEAVES, 100, level_tree, random.randrange(10, 40, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under47,
             (
                 nibs['tree'], LEAVES, random.randrange(140, 200, 20), 5, random.randrange(-55, 55, 35), palette, 10,
                 True))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

    elif LEAVES_NEEDED < 128:
        angle_range = [random.randrange(-40, -20, 10), random.randrange(20, 40, 10)]
        final_angle = random.choice(angle_range)

        functions_ = [
            (tb.sym_tree, (nibs['tree'], LEAVES, 130, level_tree, random.randrange(15, 45, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under127,
             (nibs['tree'], LEAVES, random.randrange(120, 160, 20), 6, final_angle, palette, 10, True))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

    elif LEAVES_NEEDED < 301:
        if 181 < LEAVES_NEEDED < 231:  # do not change this. Under 181 and over 231 level_tree=level_tree
            level_tree = level_tree - 1
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        final_angle = random.choice(angle_range)
        if LEAVES_NEEDED < 150:
            asym_tree_level = random.randint(5, 6)
        else:
            asym_tree_level = random.randint(6, 8)
        functions_ = [
            (tb.sym_tree, (nibs['tree'], LEAVES, 130, level_tree, random.randrange(20, 45, 5), palette, 10, 0.75)),
            (tb.asymmetric_tree_under600,
             (
                 nibs['tree'], LEAVES, random.randrange(120, 140, 20), asym_tree_level, final_angle,
                 palette,
                 10, variant))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

    elif LEAVES_NEEDED < 701:
        if 362 < LEAVES_NEEDED < 476:  # do not change this or simplify.
            level_tree = level_tree - 1
        angle_range = [random.randrange(-45, -15, 10), random.randrange(15, 45, 10)]
        final_angle = random.choice(angle_range)
        functions_ = [
            (tb.sym_tree, (nibs['tree'], LEAVES, 120, level_tree, random.randrange(20, 50, 10), palette, 10, 0.75)),
            (tb.asymmetric_tree_under600,
             (nibs['tree'], LEAVES, random.randrange(130, 140, 10), random.randint(6, 8), final_angle,
              palette, 10, variant))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

    else:
        angle_range = [random.randrange(-40, -20, 10), random.randrange(20, 40, 10)]
        final_angle = random.choice(angle_range)
        if LEAVES_NEEDED < 1500:
            level_range = random.randint(7, 8)
        else:
            level_range = random.randint(7, 9)
        functions_ = [
            (tb.sym_tree, (nibs['tree'], LEAVES, 120, level_tree, random.randrange(25, 45, 10), palette, 10, 0.8)),
            (tb.asymmetric_tree_under600, (
                nibs['tree'], LEAVES, random.randrange(130, 150, 10), level_range, final_angle,
                palette, 10, variant))
        ]

        x = random.choice(functions_)
        x[0](*x[1])

    if ROOTS_NEEDED < 48:
        if ROOTS_NEEDED < 31:
            level_root = 3
        else:
            level_root = 4
        root_pensize = 6
        root_angle = (random.randrange(25, 45, 10))
        root_length = random.randrange(70, 90, 10)
        x_coord = -300
        y_coord = -300

    elif ROOTS_NEEDED < 128:
        if ROOTS_NEEDED < 119:
            level_root = 4
        else:
            level_root = 5
        root_pensize = 10
        root_angle = (random.randrange(30, 40, 10))
        root_length = random.randrange(100, 120, 10)
        x_coord = -340
        y_coord = -340
    elif ROOTS_NEEDED < 301:
        if ROOTS_NEEDED < 180:
            level_root = 4
        else:
            level_root = 5
        root_pensize = 10
        root_angle = (random.randrange(30, 40, 10))
        root_length = random.randrange(110, 130, 10)
        x_coord = -360
        y_coord = -360
    elif ROOTS_NEEDED < 701:
        if ROOTS_NEEDED < 500:
            level_root = 5
        else:
            level_root = 6
        root_pensize = 10
        root_angle = (random.randrange(30, 40, 10))
        root_length = random.randrange(110, 130, 10)
        x_coord = -400
        y_coord = -400

    else:
        if ROOTS_NEEDED < 1150:
            level_root = 6
        elif ROOTS_NEEDED < 4000:
            level_root = 7
        else:
            level_root = 8
        root_pensize = 10
        root_angle = (random.randrange(30, 40, 10))
        root_length = random.randrange(100, 120, 10)
        x_coord = -400
        y_coord = -400

    tb.asym_roots(nib_name=nibs['root'], ROOTS=ROOTS, length=root_length, levels=level_root, angle=root_angle,
                  root_palette=root_palette, pensize=root_pensize, variant=variant)
    tb.write_labels(nib_name=nibs['trunk'], x=x_coord, y=y_coord, address=nft.address[0:6], block=nft.block)
    if root_angle < 30 and root_length >= 100:
        root_ball = "Tight Fibrous"
    if root_angle < 30 and root_length < 100:
        root_ball = "Tight Creeping"
    if 30 <= root_angle <= 40 and root_length >= 100:
        root_ball = "Adventitious"
    if 30 <= root_angle <= 40 and root_length < 100:
        root_ball = "Creeping"
    if root_angle > 40 and root_length >= 100:
        root_ball = "Loose Fibrous"
    if root_angle > 40 and root_length < 100:
        root_ball = "Loose Creeping"
    if level_tree >= 7 or level_range >= 7:
        branch_ramification = "Extensive"
    if level_tree == 6 or level_range == 6:
        branch_ramification = "Moderate"
    if level_tree < 6 or level_range < 6:
        branch_ramification = "Low"
    if abs(final_angle) < 30:
        canopy = "Vase"
    if 30 <= abs(final_angle) <= 35 and level_tree <= 7:
        canopy = "Vase"
    if 30 <= abs(final_angle) <= 35 and 9 > level_tree > 7:
        canopy = "Spreading"
    if 30 <= abs(final_angle) <= 35 and level_tree >= 9:
        canopy = "Spreading"
    if 35 < abs(final_angle) <= 45 and LEAVES_NEEDED < 1500:
        canopy = "Spreading"
    if 35 < abs(final_angle) <= 45 and LEAVES_NEEDED >= 1500:
        canopy = "Weeping"
    if abs(final_angle) > 45:
        canopy = "Weeping"
    return leaf_palette_name, root_palette_name, nft.block, root_ball, branch_ramification, canopy



async def get_svg(address):
    svg = Turtle()
    svg.setup(width=1000, height=1000)
    svg.bgcolor('black')
    nftdata = NFTData(address)
    nftdata.get_data()
    leaf_palette_name, root_palette_name, block, root_ball, branch_ramification, canopy = nft_draw(nftdata)
    return str(svg), leaf_palette_name, root_palette_name, block, root_ball, branch_ramification, canopy


# __pragma__ ('skip')
def main():
    if USE_SVG:
        from turtle_svg import Turtle as Screen
    else:
        from turtle import Screen

    screen = Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor('black')

    TEST_ALL = False
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
        # nft_draw(nftdata)
        nft_draw(nftdata, 1636525471084)
        screen.mainloop()


if __name__ == '__main__':
    import os
    from nft_data import ETHERSCAN_KEY

    try:
        os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
    except Exception as ex:
        print(ex)

    # main()
    print(get_svg('0x2eb5e5713a874786af6da95f6e4deacedb5dc246'))
# __pragma__ ('noskip')
