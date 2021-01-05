from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return """<h1><center>Paws Rescue Center 🐾</center></h1>"""

@app.route("/about")
def about():
    return """<h1>About Us: </h1>We are a non-profit organization working as an animal rescue center. 
    We aim to help you connect with purrfect furbaby for you! 
    The animals you find at our website are rescue animals which have been rehabilitated. 
    Our mission is to promote the ideology of "Adopt, don't Shop"! """


if __name__ == "__main__":
    app.run(port=3000)
