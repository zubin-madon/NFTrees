# NFTrees
Create Trees Using Python Turtle in Web

---

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

---

## Reference links:
- Transcrypt Turtle source code:  
  https://github.com/QQuick/Transcrypt/blob/master/transcrypt/modules/turtle/__init__.py  

- Starting point for demo2:  
  https://github.com/bunkahle/Transcrypt-Examples/tree/master/turtle  
