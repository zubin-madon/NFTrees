# __pragma__ ('skip')
class window:
    alert = None

class console:
    log = None
    error = None

class document:
    getElementById = None
    createElement = None
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
            document.getElementById("mintBtn").disabled = False
        except object as e:
            console.error(str(e))

    if address:
        fetch(f'/api/getdata/', _redraw, params=dict(address=address))


def get_svg(address):
    def _get_svg(raw_data):
        data = dict(raw_data)
        try:
            window.alert(data.get('status', 'Request status not available'))
        except object as e:
            console.error(str(e))

    if address:
        background = document.createElement('rect')
        background.setAttribute('width', '100%')
        background.setAttribute('height', '100%')
        background.setAttribute('fill', 'black')
        svg_element = document.getElementById("__turtlegraph__").firstChild
        if svg_element.hasChildNodes():
            svg_element.insertBefore(background, svg_element.firstChild)
            svg = document.getElementById("__turtlegraph__").innerHTML

            if svg:
                fetch(f'/api/mint/', _get_svg, method='POST', data=dict(address=address, svg=svg))
        else:
            window.alert("Please generate a NFT tree before minting!")
