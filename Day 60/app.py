from unicodedata import name
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

