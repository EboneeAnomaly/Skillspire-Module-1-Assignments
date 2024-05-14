from flask import Flask, render_template, request, url_for, redirect, session, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
app.config['SECRET_KEY'] = 'IP1010'
app.config['STATIC_FOLDER'] = 'static'
UPLOAD_FOLDER = '/Users/Ebonee/Desktop/Skillspire/FullStack Flask/FSF Assignment 5/static/pictureuploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))


with app.app_context():
    db.create_all()



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username and password:
            user = User.query.filter_by(username=username).first()

            if user and user.password == password:
                session['user_id'] = user.id 
                return redirect(url_for("home_page"))
            else:
                return render_template("loginpage.html", message="Invalid username or password")

    return render_template("loginpage.html")

    


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST": 
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        if email and username and password:

            new_user = User(email=email, username=username, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login"))
        
        else:
            return "Missing required fields", 400
    else:
        return render_template("signuppage.html")

@app.route("/home")
def home_page():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    posts = Post.query.all()
    return render_template("homepage.html", posts=posts)

        

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    post = Post.query.get_or_404(post_id)
    
    if post.user_id != session['user_id']:
        abort(403) 
    
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("home_page"))

    return render_template("edit_post.html", post=post)

@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    post = Post.query.get_or_404(post_id)
    
    if post.user_id != session['user_id']:
        abort(403) 
    
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home_page"))

@app.route("/logout")
def logout():
    session.pop('user_id', None) 
    return redirect(url_for('login'))


@app.route ("/upload", methods=["POST"])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user_id = session['user_id']

        if title and content:
            new_post = Post(title=title, content=content, user_id=user_id)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("home_page"))
        else:
            return "Title and content are required fields", 400  


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)