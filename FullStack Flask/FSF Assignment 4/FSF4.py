from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User_base.db'
db = SQLAlchemy(app)



class User_base(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)



with app.app_context():
    db.create_all()



@app.route("/userbase", methods = ["GET"])
def userBase():
    users = User_base.query.all()
    return render_template("userbase.html", users=users)



@app.route("/adduser", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_name = f"{firstname} {lastname}"
        new_user = User_base(email=email, created_at=created_at, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()

        users = User_base.query.all()
        return render_template("userbase.html", users = users)
    
    return render_template("adduser.html")



@app.route("/users/<int:id>", methods=["GET", "POST"])
def userInfo(id):
    user = User_base.query.get_or_404(id)
    if request.method == "POST":
        user.full_name = request.form["full_name"]
        user.email = request.form["email"]
        db.session.commit()
        return redirect("/userbase")
    return render_template("users.html", user=user)


@app.route("/users/<int:id>/destroy", methods=["POST"])
def delete_user(id):
    user = User_base.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("userBase"))

@app.route("/users/<int:id>")
def show_user(id):
    user = User_base.query.get_or_404(id)
    return render_template("users.html", user=user)

@app.route("/edituser/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    user = User_base.query.get_or_404(id)
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        user.full_name = f"{firstname} {lastname}"
        user.email = email
        db.session.commit()
        return redirect(url_for("userBase"))
    else:
        return render_template("edituser.html", user=user)


@app.route("/update_user/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User_base.query.get_or_404(id)
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        print("Received form data - First Name:", firstname, "Last Name:", lastname, "Email:", email)
        

        user.full_name = f"{firstname} {lastname}"
        user.email = email
        db.session.commit()

        print(f"User {user.id} updated - Name: {user.full_name}, Email: {user.email}")


        return redirect(url_for("userBase"))
    else:
        return render_template("edituser.html", user=user)

    




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)