# __pragma__ ('skip')
import requests
import os
from web3 import Web3


# -------Key, Etherscan API URLs------------------------
test_data = dict(
    vip_address2='0x57076ca7a26c16bf301b6d1a7bef96e265d30c3e',
    vip_address3='0x2eb5e5713a874786af6da95f6e4deacedb5dc246',  # -- vip address cobie for testing
    vip_address='0x650dCdEB6ecF05aE3CAF30A70966E2F395d5E9E5', #---for testing
    vip4='0x148e2ED011A9EAAa200795F62889D68153EEacdE', #---for testing
    coin_artist='0x8443379cbaf7a68b2cc1626df9e4cb47d525a0e4', #---for testing
    NSF_address='0x32cc2ec897f21a77a704e9a7313af6a640c47bb5', #---for testing
    ultra_rare='0x96fdfd3bc8cd692aceb37a04d2be5e0bcff2172d',  # this address has only erc1155 tokens which don't show up.
)

ETHERSCAN_URL = f'https://api.etherscan.io'
ETHERSCAN_KEY = 'C431S5DRCQ7XWIXT2144ZFT9IYBJKKG1VK'

'''15 aug- 2021 Zubin added Infura URL to get 'Current Block Number'. On each artwork (tree) below the 5 chars of address, we will also print current block number which serves as a timestamp.
So if the user's wallet gets additional tokens in future and user generates a new tree, they can see the change in wallet tree patterns over time.'''

project_id = '4a337ee2c0fa4f44821a55d4bb824708'
infura_url = f"https://mainnet.infura.io/v3/{project_id}"
w3 = Web3(Web3.HTTPProvider(infura_url))
CURRENT_BLOCK = w3.eth.block_number


DEFAULT_ADDRESS = test_data['vip_address3']
# __pragma__ ('noskip')

# __pragma__ ('ecom')
#?CURRENT_BLOCK = None
#?DEFAULT_ADDRESS = '0x'
# __pragma__ ('noecom')


class NFTData:
    def __init__(self, address=DEFAULT_ADDRESS, data=''):
        self.address = address
        self.data = data
        self.block = w3.eth.block_number

    # __pragma__ ('skip')
    def get_data(self):
        try:
            api_key = os.environ['ETHERSCAN_KEY']
        except KeyError as e:
            print("KeyError:", e)
            return

        try:
            nft_token_transfer_url = f'/api?module=account&action=tokennfttx&address={self.address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
            response = requests.get(ETHERSCAN_URL + nft_token_transfer_url)
            data = response.json()
            self.data = data['result']

        except Exception as e:
            print(e)
    # __pragma__ ('noskip')

    @property
    def nft_tokens_list(self):
        return [self.data[i]['contractAddress'] for i in range(len(self.data))]

    @property
    def from_address_list(self):
        return [self.data[i]['from'] for i in range(len(self.data))]

    @property
    def token_name_list(self):
        return [self.data[i]['tokenName'] for i in range(len(self.data))]

    @property
    def token_id_list(self):
        return [self.data[i]['tokenID'] for i in range(len(self.data))]

    @property
    def token_symbol_list(self):
        return [self.data[i]['tokenSymbol'] for i in range(len(self.data))]

    @property
    def timestamp_list(self):
        return [self.data[i]['timeStamp'] for i in range(len(self.data))]


# __pragma__ ('skip')
if __name__ == '__main__':
    try:
        os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
    except Exception as ex:
        print(ex)

    nft = NFTData()
    nft.get_data()
    # print(nft.data)
    print("nft_tokens_list:", nft.nft_tokens_list)
    print("from_address_list:", nft.from_address_list)
    print("token_name_list:", nft.token_name_list)
    print("token_id_list:", nft.token_id_list)
    print("token_symbol_list:", nft.token_symbol_list)
    print("timestamp_list:", nft.timestamp_list)
# __pragma__ ('noskip')
