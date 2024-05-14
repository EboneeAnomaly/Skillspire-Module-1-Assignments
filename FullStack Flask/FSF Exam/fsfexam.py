from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Patient_base.db'
db = SQLAlchemy(app)

class Patient_base(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    complaint = db.Column(db.String(100), nullable=False)
    
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return redirect(url_for('patientBase'))

@app.route("/patientbase", methods = ["GET"])
def patientBase():
    patients = Patient_base.query.all()
    return render_template("patientbase.html", patients=patients)


@app.route("/newappointment", methods = ["GET", "POST"])
def addAppointment():
    if request.method == "POST":
        date = request.form.get("date")
        time = request.form.get("time")
        patient_name = request.form.get("patient_name")
        complaint = request.form.get("complaint")

        if not (date and time and patient_name and complaint):
            return "All fields are required. Please fill out the form completely.", 400
        
        new_appointment = Patient_base(date=date, time=time, patient_name=patient_name, complaint=complaint)
        
        db.session.add(new_appointment)
        db.session.commit()
        
        return redirect(url_for('patientBase'))
    
    
    return render_template("newappointment.html")



@app.route("/cancelappointment/<int:appointment_id>", methods=["POST"])
def cancelAppointment(appointment_id):
    return redirect(url_for('patientBase'))


@app.route("/deleteappointment/<int:appointment_id>", methods =["POST"])
def deleteAppointment(appointment_id):
    return redirect(url_for('patientbase'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)