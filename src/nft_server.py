from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

from nft_data import NFTData, ETHERSCAN_KEY
from nft_art import get_svg


'''Convert paths below to absolute paths while testing on local machine'''
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
        return dict(address=nft.address, data=nft.data, block=nft.block)
    return dict(address='', data='', block='')


@app.post("/api/draw/")
async def draw_svg(address: str = Form(...)):
    if address:
        svg_data = await get_svg(address)
        return dict(address=address, svg=svg_data[0], leaf_palette_name=svg_data[1], root_palette_name=svg_data[2], block=svg_data[3], root_ball=svg_data[4], branch_ramification=svg_data[5], canopy=svg_data[6])
    return dict(address='', data='')


class MintData(BaseModel):
    address: str
    svg: str


@app.post("/api/mint/")
async def get_data(svg_data: MintData):
    if svg_data:
        if svg_data.address and svg_data.svg:
            try:
                # Instead of saving locally, code to upload SVG to IPFS would go here
                with open(f'{svg_data.address}.svg', 'w') as f:
                    f.write(svg_data.svg)
            except Exception as e:
                print("ERROR:", e)
                return dict(status='FAILED')

            return dict(status='SUCCESS')
    return dict(status='FAILED')


# run from terminal with:  uvicorn  --app-dir src nft_server:app --reload
