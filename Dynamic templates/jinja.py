"""
    Delimiters
        {% ... %} is used for statements.
        {{ ... }} is used for variables.
        {# ... #} is used for comments.
        # ... ## is used for line statements.
"""

from flask import Flask , render_template

arr =  ["Ved" , "Gupta"]
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html" , name = "Ved Gupta")


@app.route('/see')
def new():
    return render_template("index.html" , name = arr[0])

if __name__ == "__main__":
    app.run(port = 3000)
