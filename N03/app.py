from flask import Flask, render_template, url_for, redirect, request, send_from_directory
from werkzeug.utils import secure_filename
import os.path

# CAPS means constant values
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(['bmp', 'gif', 'jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = os.path.join(FILE_DIR ,'static\\images')

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student/")
def student():
    return render_template("student.html")

@app.route("/teacher/")
def teacher():
    return render_template("teacher.html")

@app.route("/form/", methods = ["GET", "POST"])
def form():
    if request.method == "GET": # only enter website
        return render_template("message_form.html")
    else: # POST --> form is filled
        username = request.form["username"]
        email = request.form["email"]
        message = request.form["message"]
        return render_template("message_result.html", username = username, email = email, message = message)

@app.route("/upload/", methods = ["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        picture = request.files["picture"]
        # checks that filename is not empty
        if picture.filename != "": # checks that the file extension is of defined type
            if picture.filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS:
                file = secure_filename(picture.filename)
                picture.save(os.path.join(UPLOAD_FOLDER, file))
                return render_template("upload_result.html", picture = "/images/" + file)
            else:
                return render_template("upload_result.html", picture = False)
        else:
            return render_template("upload_result.html", picture = None)

@app.route('/showfile/<filename>')
def showfile(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

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