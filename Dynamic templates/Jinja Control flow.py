"""
Loops #
The syntax of for loops in Jinja is very similar to pythonic syntax.

{% for elements in array %}
    ...
{% endfor %}

📌 Note: You must always end the for loop using {% endfor %}.

"""
from flask import Flask ,render_template

value = {
    "Name " : "Ved Prakash Gupta",
    "Age" : "19",
    "College" : "Galgotias College of Engineering and Technology",
    "Branch": "Information Technology"
    }

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html" , data = value )


if __name__ == "__main__":
    app.run()
