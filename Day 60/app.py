from unicodedata import name
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder="template")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run()
