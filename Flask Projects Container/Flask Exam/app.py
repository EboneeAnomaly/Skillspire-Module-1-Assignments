from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'user_login_store'

USERNAME = "admin"
PASSWORD = "password"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/index")
def index():
    name = request.args.get('name')
    return render_template("index.html", name=name)

@app.route("/greet/<name>", methods=["POST", "GET"])
def greet(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    form_data = {
    'firstname': request.form.get("firstname"),
    'lastname':  request.form.get("lastname"),
    'phonenumber': request.form.get("phonenumber"),
    'streetaddress': request.form.get("streetaddress"),
    'state': request.form.get("state"),
    'zipcode': request.form.get("zipcode"),
    }

    return render_template("submit_contact.html", form_data=form_data)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for("admin"))
        else:
            return "Incorrect entry, please try again."
    return render_template("login.html")

@app.route("/admin")
def admin():
    if session.get('logged_in'):
        return "Admin Panel: User is logged in"
    else:
        return "Admin Panel: User is not logged in"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)