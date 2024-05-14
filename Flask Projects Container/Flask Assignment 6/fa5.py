from flask import Flask, render_template, sessions
fa5 = Flask(__name__)

@fa5.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    fa5.run(debug=True, host="0.0.0.0", port=5000)

