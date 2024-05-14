from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '54321stkyone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

with app.app_context():
    db.drop_all() 
    db.create_all()


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        new_user = User(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('userinfo'))

    return render_template("signup.html")

@app.route("/userinfo")
def userinfo():
    users = User.query.all()
    return render_template("userinfo.html", users=users)


@app.route("/greeting/<username>", methods=["GET", "POST"])
def greeting(username):
    return render_template("greeting.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return redirect(url_for('greeting', username=username))
        else:
            print("No user found")
            error_message = "No user found, please try again"
            return render_template("login.html", error_message=error_message)
           
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)