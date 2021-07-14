from flask import Flask, url_for, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        db = sqlite3.connect("DATABASE.db")
        query = """
                INSERT INTO Person("Name", "Age")
                VALUES(?, ?)
                """
        db.execute(query, (request.form["name"], request.form["age"]))
        db.commit()
        db.close()
        return redirect(url_for("result"))

@app.route("/result/")
def result():
    db = sqlite3.connect("DATABASE.db")
    query = """
            SELECT *
            FROM Person
            """
    result = list(db.execute(query))
    db.close()
    return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run()
