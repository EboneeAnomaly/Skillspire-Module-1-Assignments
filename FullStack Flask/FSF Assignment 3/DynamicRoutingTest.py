from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"Course Name": 'How to be a Ninja', "Description": 'blank', "Date Added": 'Dec. 1st 2013 5:34PM', "Actions": 'Remove'},
    {"Course Name": 'How to fly', "Description": 'blank', "Date Added": 'Nov. 1st 2011 11:12AM', "Actions": 'Remove'},
    {"Course Name": 'How to get more energy in the bootcamp', "Description": 'blank', "Date Added": 'Oct. 1st 2013 11:11AM', "Actions": 'Remove'},
    {"Course Name": 'How to pair programs more effectively', "Description": 'blank', "Date Added": 'Sept. 28th 2011 10:15PM', "Actions": 'Remove'}
]

@app.route("/newcourse")
def createCourse():
    return render_template("newcourse.html", courses=courses)

@app.route("/destroy")
def deletepage():
    return render_template("destroy.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)