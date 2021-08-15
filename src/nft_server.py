from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from nft_data import NFTData, ETHERSCAN_KEY


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"))
app.mount("/__target__", StaticFiles(directory="src/__target__"))


try:
    os.environ['ETHERSCAN_KEY'] = ETHERSCAN_KEY
except Exception as ex:
    print(ex)


@app.get("/")
async def index():
    print("DEFAULT ROUTE")
    return FileResponse('./src/static/index.html', media_type='text/html')


@app.get("/api/getdata/")
async def get_data(address=None):
    if address:
        nft = NFTData(address)
        nft.get_data()
        return dict(address=nft.address, data=nft.data)
    return dict(address='', data='')


# run from terminal with:  uvicorn  --app-dir src nft_server:app --reload
