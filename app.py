from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    submitted_url = None
    if request.method == "POST":
        submitted_url = request.form.get("url")
    return render_template("index.html", submitted_url=submitted_url)

if __name__ == "__main__":
    app.run(debug=True)