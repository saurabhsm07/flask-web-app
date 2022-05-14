from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>make way for the king !!!!</h1>"


@app.route("/about")
def about():
    return "<h1> He is your king !!!!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
