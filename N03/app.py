from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student/")
def student():
    return render_template("student.html")

@app.route("/teacher/")
def teacher():
    return render_template("teacher.html")

@app.route('/display/<role>')
def display(role):
    if role == 'student': # search student function, print url for student (url_for)
        return redirect(url_for('student')) # redirect /display/student to /student
    elif role == 'teacher':  # search student function, print url for teacher
        return redirect(url_for('teacher'))  # redirect /display/teacher to /teacher
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug = True)