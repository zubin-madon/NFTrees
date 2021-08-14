import requests

# -------Key, Etherscan API URLs------------------------

key = 'C431S5DRCQ7XWIXT2144ZFT9IYBJKKG1VK'
address = '0x148e2ED011A9EAAa200795F62889D68153EEacdE'
vip_address2 = '0x57076ca7a26c16bf301b6d1a7bef96e265d30c3e'
vip_address3 = '0x2eb5e5713a874786af6da95f6e4deacedb5dc246'  # -- vip address cobie
vip_address = '0x650dCdEB6ecF05aE3CAF30A70966E2F395d5E9E5'
vip4 = '0x148e2ED011A9EAAa200795F62889D68153EEacdE'
coin_artist = '0x8443379cbaf7a68b2cc1626df9e4cb47d525a0e4'
NSF_address = '0x32cc2ec897f21a77a704e9a7313af6a640c47bb5'
ultra_rare = '0x96fdfd3bc8cd692aceb37a04d2be5e0bcff2172d' #only 1159
etherscan_url = f'https://api.etherscan.io'
nft_token_transfer_url = f'/api?module=account&action=tokennfttx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey={key}'

response = requests.get(url=etherscan_url + nft_token_transfer_url)
data = response.json()
number_of_nft_txns = len(data['result'])

# --------------- Lists of retrieved data ------------------
nft_tokens_list = [data['result'][i]['contractAddress'] for i in range(number_of_nft_txns)]
from_address_list = [data['result'][i]['from'] for i in range(number_of_nft_txns)]
token_name_list = [data['result'][i]['tokenName'] for i in range(number_of_nft_txns)]
token_id_list = [data['result'][i]['tokenID'] for i in range(number_of_nft_txns)]
token_symbol_list = [data['result'][i]['tokenSymbol'] for i in range(number_of_nft_txns)]
timestamp_list = [data['result'][i]['timeStamp'] for i in range(number_of_nft_txns)]

