from flask import Flask

app = Flask(__name__)

@app.route("/")
def sendheyy():
    return "heyys guys i am flask"

@app.route("/one")
def name():
    return "My Name is Flask\n I am Micro FrameWork"

if __name__ == "__main__":
    app.run(port = 3000)
