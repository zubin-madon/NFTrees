# __pragma__ ('skip')
class console:
    log = None
    error = None
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
