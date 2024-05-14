from flask import Flask, render_template, url_for, redirect, request, abort, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from datetime import datetime
from flask_login import login_user
from werkzeug.security import check_password_hash
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'tp1989'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guest_info.db'


db = SQLAlchemy(app)

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


with app.app_context():
    db.create_all()

@app.route("/guests/<int:post_id>", methods=["GET"])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template("guests.html", post=post, comments=comments)


@app.route("/guests/<int:post_id>/add_comment", methods=["POST"])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form['content']
    comment = Comment(content=content, author_id=current_user.id, post_id=post.id)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('view_post', post_id=post_id))

@app.route("/guests/<int:comment_id>/edit_comment", methods=["GET", "POST"])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author_id != current_user.id:
        abort(403) 
    if request.method == "POST":
        comment.content = request.form['content']
        db.session.commit()
        return redirect(url_for('guests'))
    return render_template('edit_comment.html', comment=comment)

@app.route("/guests/<int:comment_id>/delete_comment", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author_id != current_user.id:
        abort(403) 
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('view_post', post_id=comment.post_id))



@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/guests")
def guests():
    guests = Guest.query.all()
    return render_template("guests.html", guests=guests)
    

@app.route("/guests/<int:post_id>/edit_guest", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("edit_guest.html", post=post)



@app.route("/guests/<int:guest_id>/update", methods=["POST"])
def update_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    guest.email = request.form['email']
    guest.username = request.form['username']
    guest.password = request.form['password']
    db.session.commit()
    return redirect(url_for('guests'))


@app.route("/guests/<int:guest_id>/delete", methods=["POST"])
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    db.session.delete(guest)
    db.session.commit()
    return redirect(url_for('guests'))

    

@app.route("/guests/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("guests"))

@app.route("/shop")
def shopping():
    return render_template("shop.html")


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        existing_user = Guest.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please choose a different one.', 'error')
            return redirect(url_for('signup'))

        new_user = Guest(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('home'))  

    return render_template("signup.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = Guest.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        login_user(user)
        flash('Welcome back to the Great Northern Lodge', 'success')
        return redirect(url_for("guests"))
    else:
        flash('Invalid username or password. Please try again.', 'error')
        return redirect(url_for('home'))

@app.route("/popup-message", methods=["GET"])
def popup_message():
    messages = [(msg, category) for msg, category in get_flashed_messages(with_categories=True)]
    return jsonify(messages)



@app.route("/guests/<int:guest_id>/edit", methods=["GET", "POST"])
def edit_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    
    if request.method == "POST":
        guest.email = request.form['email']
        guest.username = request.form['username']
        guest.password = request.form['password']
        
        db.session.commit()
        
        return redirect(url_for('guests'))
    
    return render_template("edit_guest.html", guest=guest)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)