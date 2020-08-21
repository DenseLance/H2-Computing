from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/rp_calc/", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        return render_template("calculator_set.html", \
            PW = request.form["PW"], \
            MT = request.form["MT"])
    else:
        return render_template("calculator.html")

@app.route('/rp_display/', methods = ["GET", "POST"])
def display():
    if request.method == "POST":
        return render_template("calculator_result.html", \
            h2_subject_1 = request.form["H2 Subject 1"], \
            h2_subject_2 = request.form["H2 Subject 2"], \
            h2_subject_3 = request.form["H2 Subject 3"], \
            h1_subject = request.form["H1 Subject"], \
            general_paper = request.form["General Paper"], \
            project_work = request.form["Project Work"], \
            mother_tongue = request.form["Mother Tongue"])
    else:
        return redirect(url_for('form'))

if __name__ == "__main__":
    app.run(debug = True)