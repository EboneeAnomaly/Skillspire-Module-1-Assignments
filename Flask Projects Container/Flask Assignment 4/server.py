from flask import Flask, render_template

server = Flask(__name__)

@server.route("/")
def index():
    return render_template("index.html")

@server.route("/displayname")
def display_name():
    return render_template("display-name.html")

@server.route("/displayfood")
def display_food():
    return render_template("display-food.html")

@server.route("/displayvacation")
def display_vacation():
    return render_template("display-vacation.html")

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)