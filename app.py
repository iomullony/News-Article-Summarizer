from flask import Flask, redirect, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    submitted_url = None
    if request.method == "POST":
        submitted_url = request.form.get("url")
        r = requests.get(submitted_url)
        soup = BeautifulSoup(r.text, "html.parser")
        return render_template("index.html", submitted_url=soup.article.get_text())
    else: 
        return render_template("index.html", submitted_url=None)
