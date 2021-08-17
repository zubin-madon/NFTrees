# NFTrees
Create Trees Using Python Turtle in Web

---
Download font rootbeer.ttf in main

### Setup Virtual Environment
_For Linux/Mac:_  
$ `python3.9 -m venv venv`  
$ `source ./venv/bin/activate`

_For Windows:_  
\> `py -3.9 -m venv venv`  
\> `.\venv\Scripts\activate`

_Install Transcrypt:_  
(venv) $ `pip install transcrypt`

_To exit virtual environment:_  
(venv) $ `deactivate`  
$

---

### demo1 - Snowflake
(venv) $ `transcrypt --nomin --map src/demos/demo1`  
(venv) $ `python -m http.server -d ./src/demos`

http://localhost:8000/demo1.html


### demo2 - Tree (with user input)
(venv) $ `transcrypt --nomin --map src/demos/demo2`  
(venv) $ `python -m http.server -d ./src/demos`

http://localhost:8000/demo2.html

_To generate minified JavaScript w/o sourcemaps, just leave off the flags when running Transcrypt:_  
(venv) $ `transcrypt src/demo2` 


### Main App
- _**nft_art.py**_ - entry point (works on both server & client)
- _**tree_builders.py**_ - tree building algorithms (works on both server & client)
- _**nft_data.py**_ - Class to retrieve and parse NFT data
  - works on both server & client
  - use a seed value as second parameter to repeat tree build
  - add `?seed=123` to `/` URL to get repeatable tree builds in browser (use any # for seed value)
  - Change `TEST_ALL` variable to `True` to run all wallet IDs in `nft_data.test_data`
- _**urlutils.py**_ - client side ajax helper functions (gets transpiled)  
- _**app.py**_ - client side web application (transpiled files get put into `./src/__target__/`)  
  (venv) $ `transcrypt --nomin --map src/app.py`  
- _**nft_server.py**_ - FastAPI REST server  
  (venv) $ `uvicorn  --app-dir src nft_server:app --reload`  
  http://localhost:8000  
---

## Reference links:
- Transcrypt Turtle source code:  
  https://github.com/QQuick/Transcrypt/blob/master/transcrypt/modules/turtle/__init__.py  

- Starting point for demo2:  
  https://github.com/bunkahle/Transcrypt-Examples/tree/master/turtle
  
- NFT minting and wallet integration A-Z resource:
  https://github.com/austintgriffith/scaffold-eth/tree/simple-nft-example
