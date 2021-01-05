from flask import Flask

app = Flask(__name__)

@app.route("/")
def wel():
    return "Welcome to the Page"

@app.route("/<data>")
def value(data):
    """Fuction return the value in data"""
    return data

# ----------------------------------------------
""" there are different Converters can accept different data types as a parameter
     String ----> Default behavior
     int    ----> Accepts only positive integer
     float  ----> Accepts only positive Floating point numbers
     path   ----> Accepts String with slashes
     uuid   ----> Accepts UUID Stings

"""

# -------------------------------------------------

@app.route("/string/<string:a>")
def aa(a):
    return "this only accept string. Your String : " + a

@app.route("/int/<int:b>")
def bb(b):
    return "this only accept Positive int. Your int : " + str(b)

@app.route("/float/<float:c>")
def c(c):
    return "this only accept Positive Float. Your Float : " + str(c)

@app.route("/path/<path:d>")
def dd(d):
    return "this only accept path. Your path : " + d

@app.route("/uuid/<uuid:e>")
def ee(e):
    return "this only accept uuid String. Your uuid String : " + e

if __name__ == "__main__":
    app.run(port = 3000)
