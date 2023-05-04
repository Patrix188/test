from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.jinja.html")

@app.route("/learning/")
def learning():
    return render_template("learning.jinja.html")

@app.route("/holyShit/")
def holyshit():
    return render_template("holyShit.jinja.html")