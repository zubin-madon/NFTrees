from fastapi import FastAPI
import os

from nft_data import NFTData, ETHERSCAN_KEY


app = FastAPI()


try:
    os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
except Exception as ex:
    print(ex)


@app.get("/")
async def get_data():
    return {"OK"}


@app.get("/api/getdata/")
async def get_data(address=None):
    if address:
        nft = NFTData(address)
        nft.get_data()
        return dict(address=nft.address, data=nft.data)
    return dict(address='', data='')


# run from terminal with:  uvicorn  --app-dir src nft_server:app --reload
