from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/kyuuyo")
def kyuuyo():
    return render_template("kyuuyo.html")

# @app.route("/")

if __name__ == "__main__":
    app.run(debug=True)