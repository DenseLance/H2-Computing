from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/student/")
def student():
    return render_template("student.html")

@app.route("/teacher/")
def teacher():
    return render_template("teacher.html")

if __name__ == "__main__":
    app.run(debug = True)