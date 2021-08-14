import requests


# -------Key, Etherscan API URLs------------------------

# vip_address2 = '0x57076ca7a26c16bf301b6d1a7bef96e265d30c3e'
# vip_address3 = '0x2eb5e5713a874786af6da95f6e4deacedb5dc246'  # -- vip address cobie
# vip_address = '0x650dCdEB6ecF05aE3CAF30A70966E2F395d5E9E5'
# vip4 = '0x148e2ED011A9EAAa200795F62889D68153EEacdE'
# coin_artist = '0x8443379cbaf7a68b2cc1626df9e4cb47d525a0e4'
# NSF_address = '0x32cc2ec897f21a77a704e9a7313af6a640c47bb5'
# ultra_rare = '0x96fdfd3bc8cd692aceb37a04d2be5e0bcff2172d'  # only 1159
TEST_ADDRESS = '0x148e2ED011A9EAAa200795F62889D68153EEacdE'
ETHERSCAN_URL = f'https://api.etherscan.io'
API_KEY = 'C431S5DRCQ7XWIXT2144ZFT9IYBJKKG1VK'


class NFTData:
    def __init__(self, address=TEST_ADDRESS):
        self.address = address
        nft_token_transfer_url = f'/api?module=account&action=tokennfttx&address={self.address}&startblock=0&endblock=999999999&sort=asc&apikey={API_KEY}'
        self.url = ETHERSCAN_URL + nft_token_transfer_url
        self.transaction_qty = 0
        self.data = None

    def get_data(self):
        response = requests.get(self.url)
        data = response.json()
        self.data = data['result']
        self.transaction_qty = len(self.data)

    @property
    def nft_tokens_list(self):
        return [self.data[i]['contractAddress'] for i in range(self.transaction_qty)]

    @property
    def from_address_list(self):
        return [self.data[i]['from'] for i in range(self.transaction_qty)]

    @property
    def token_name_list(self):
        return [self.data[i]['tokenName'] for i in range(self.transaction_qty)]

    @property
    def token_id_list(self):
        return [self.data[i]['tokenID'] for i in range(self.transaction_qty)]

    @property
    def token_symbol_list(self):
        return [self.data[i]['tokenSymbol'] for i in range(self.transaction_qty)]

    @property
    def timestamp_list(self):
        return [self.data[i]['timeStamp'] for i in range(self.transaction_qty)]


if __name__ == '__main__':
    nft = NFTData()
    nft.get_data()
    print("nft_tokens_list:", nft.nft_tokens_list)
    print("from_address_list:", nft.from_address_list)
    print("token_name_list:", nft.token_name_list)
    print("token_id_list:", nft.token_id_list)
    print("token_symbol_list:", nft.token_symbol_list)
    print("timestamp_list:", nft.timestamp_list)
