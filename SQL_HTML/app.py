from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/sign_in/", methods = ["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html", enter = None)
    elif request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            message = request.form["message"]

            db = sqlite3.connect("database.db")
            query = f"""
            SELECT username, password
            FROM UserInfo
            WHERE username = '{username}'
            AND password = '{password}'
            """
            cursor = db.execute(query)
            user = cursor.fetchone()
            db.close()

            if username == user[0] and password == user[1]:
                db = sqlite3.connect("database.db")
                query = f"""
                INSERT INTO Forum (username, message)
                VALUES (?, ?)
                """
                db.execute(query, (username, message))
                db.commit()
                db.close()
                return render_template("sign_in.html", enter = True)
            else:
                return render_template("sign_in.html", enter = False)
        except:
            return render_template("sign_in.html", enter = False)

@app.route("/sign_up/", methods = ["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html", create_account = None)
    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            db = sqlite3.connect("database.db")
            query = f"""
            INSERT INTO UserInfo (username, email, password)
            VALUES (?, ?, ?)
            """
            db.execute(query, (username, email, password))
            db.commit()
            db.close()
            return render_template("sign_up.html", create_account = True)    
        except:
            return render_template("sign_up.html", create_account = False)

@app.route("/")
def forum():
    db = sqlite3.connect("database.db")
    query = "SELECT * FROM Forum"
    cursor = db.execute(query)
    board = cursor.fetchall()
    db.close()
    return render_template("forum.html", board = board)
        
if __name__ == "__main__":
    app.run(debug = True)