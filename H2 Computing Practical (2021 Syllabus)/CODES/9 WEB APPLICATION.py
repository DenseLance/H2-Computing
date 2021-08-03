from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/html_form/", methods = ["GET", "POST"])
def html_form():
    if request.method == "GET":
        return render_template("html_form.html")
    else:
        name = request.form["name"] # text
        age = request.form["age"] # number
        gender = request.form["gender"] # radio
        class_ = request.form["class"] # dropdown
        colour = request.form.getlist("colour") # checkbox, getlist
        email = request.form["email"] # email
        dob = request.form["dob"] # date
        feedback = request.form["feedback"] # textarea
        # submit, reset
        
        return render_template("html_form_result.html",
                               name = name,
                               age = age,
                               gender = gender,
                               class_ = class_,
                               colour = colour,
                               email = email,
                               dob = dob,
                               feedback = feedback)

@app.route("/file_upload/", methods = ["GET", "POST"])
def file_upload():
    if request.method == "GET":
        return render_template("file_upload.html")
    else:
        img_file = request.files["img_file"]
        doc_file = request.files["doc_file"]

        if img_file.filename != "": # checks that filename is not empty
            img_file.save("static/images/" + img_file.filename) # save file in static

        if doc_file.filename != "": # checks that filename is not empty
            doc_file.save("static/others/document.docx") # save file in static
    
        return render_template("file_upload_result.html", img_file_location = "images/" + img_file.filename)

@app.route("/display/<action>/")
def display(action):
    if action == "html_form":
        return redirect(url_for("html_form"))
    elif action == "file_upload":
        return redirect(url_for("file_upload"))
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
