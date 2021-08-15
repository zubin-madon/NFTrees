# __pragma__ ('skip')
class console:
    log = None
    error = None

class document:
    getElementById = None
# __pragma__ ('noskip')

from urlutils import fetch
from nft_data import NFTData
from nft_art import nft_draw


def redraw(address):

    def _redraw(raw_data):
        data = dict(raw_data)
        try:
            nftdata = NFTData(data['address'], data['data'])
            nft_draw(nftdata)
        except object as e:
            console.error(str(e))

    if address:
        fetch(f'/api/getdata/', _redraw, params=dict(address=address))


def get_svg(address):
    def _get_svg(raw_data):
        data = dict(raw_data)
        try:
            console.log(data)
        except object as e:
            console.error(str(e))

    if address:
        svg = document.getElementById("__turtlegraph__").innerHTML

        if svg:
            fetch(f'/api/mint/', _get_svg, method='POST', data=dict(address=address, svg=svg))


