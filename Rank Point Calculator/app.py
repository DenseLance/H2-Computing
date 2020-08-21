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
        PW = request.form["PW"]
        MT = request.form["MT"]
        return render_template("calculator_set.html", PW = PW, MT = MT)
    else:
        return render_template("calculator.html")

@app.route('/rp_display/', methods = ["GET", "POST"])
def display():
    if request.method == "POST":
        h2_subject_1 = request.form["H2 Subject 1"]
        h2_subject_2 = request.form["H2 Subject 2"]
        h2_subject_3 = request.form["H2 Subject 3"]
        h1_subject = request.form["H1 Subject"]
        general_paper = request.form["General Paper"]
        try:
            project_work = request.form["Project Work"]
        except:
            project_work = None
        try:
            mother_tongue = request.form["Mother Tongue"]
        except:
            mother_tongue = None
        
        h2 = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "S": 5, "U": 0}
        h1 = {"A": 10, "B": 8.75, "C": 7.5, "D": 6.25, "E": 5, "S": 2.5, "U": 0}

        h2_subject_1_score = h2[h2_subject_1]
        h2_subject_2_score = h2[h2_subject_2]
        h2_subject_3_score = h2[h2_subject_3]
        h1_subject_score = h1[h1_subject]
        general_paper_score = h1[general_paper]

        rank_point = h2_subject_1_score + h2_subject_2_score + h2_subject_3_score + h1_subject_score + general_paper_score
        max_rank_point = 90

        if project_work == None:
            max_rank_point -= 10
            project_work_score = 0
        else:
            project_work_score = h1[project_work]
            rank_point += project_work_score

        if mother_tongue == None:
            mother_tongue_score = 0
        else:
            rank_point_2 = rank_point
            mother_tongue_score = h1[mother_tongue]
            rank_point += mother_tongue_score
            rank_point = rank_point / (max_rank_point + 10) * max_rank_point
            if rank_point_2 > rank_point:
                rank_point = rank_point_2

        # formatting
        h2_subject_1_score = "{:.2f}".format(h2_subject_1_score)
        h2_subject_2_score = "{:.2f}".format(h2_subject_2_score)
        h2_subject_3_score = "{:.2f}".format(h2_subject_3_score)
        h1_subject_score = "{:.2f}".format(h1_subject_score)
        general_paper_score = "{:.2f}".format(general_paper_score)
        project_work_score = "{:.2f}".format(project_work_score)
        mother_tongue_score = "{:.2f}".format(mother_tongue_score)
        rank_point = "{:.2f}".format(rank_point)
        max_rank_point = "{:.2f}".format(max_rank_point)

        return render_template("calculator_result.html", h2_subject_1 = h2_subject_1, h2_subject_2 = h2_subject_2, h2_subject_3 = h2_subject_3, h1_subject = h1_subject, general_paper = general_paper, project_work = project_work, mother_tongue = mother_tongue, h2_subject_1_score = h2_subject_1_score, h2_subject_2_score = h2_subject_2_score, h2_subject_3_score = h2_subject_3_score, h1_subject_score = h1_subject_score, general_paper_score = general_paper_score, project_work_score = project_work_score, mother_tongue_score = mother_tongue_score, rank_point = rank_point, max_rank_point = max_rank_point)
    else:
        return redirect(url_for('form'))

if __name__ == "__main__":
    app.run()