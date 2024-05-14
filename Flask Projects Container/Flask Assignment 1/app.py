from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'user_info_store'

@app.route("/home")
def about_me():
    return render_template("Home.html")

@app.route("/form")
def form():
    form_data = session.get('form_data', {})
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    favoritefood = request.form.get("favoritefood")

    session['user_submitted_data'] = {
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'favoritefood': favoritefood,
    }
    return render_template("submit.html", firstname=firstname,lastname=lastname, email=email, favoritefood=favoritefood)
    

@app.route("/userform")
def user_form():
    return render_template("User Form.html")

@app.route("/user submit", methods=["POST"])
def user_submit():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    homeaddress = request.form.get("homeaddress")
    city = request.form.get("city")
    state = request.form.get("state")
    zipcode = request.form.get("zipcode")
    gender = request.form.get("gender")
    return render_template("user submit.html", firstname=firstname,lastname=lastname, email=email, homeaddress=homeaddress, city=city, state=state, zipcode=zipcode, gender=gender)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)