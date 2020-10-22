from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def forum():
    db = sqlite3.connect("database.db")
    query = "SELECT * FROM Forum"
    cursor = db.execute(query)
    board = cursor.fetchall()
    db.close()
    return render_template("forum.html", board = board)

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

@app.route("/update/", methods = ["GET", "POST"])
def update():
    if request.method == "GET":
        # display form to get id and new msg
        return render_template("update.html", updated = None)
    else:
        # process submitted data and save to db
        username = request.form["username"]
        password = request.form["password"]
        message_id = request.form["message_id"]
        message = request.form["message"]

        try:
            db = sqlite3.connect("database.db")
            query = f"""
            UPDATE Forum
            SET message = ?
            WHERE id = ?
            """
            db.execute(query, (message, message_id))
            db.commit()
            db.close()
            return render_template("update.html", updated = True)
        except:
            return render_template("update.html", updated = False)

@app.route("/delete/", methods = ["GET", "POST"])
def delete():
    if request.method == "GET":
        # display form to get id and new msg
        return render_template("delete.html", deleted = None)
    else:
        # process submitted data and save to db
        username = request.form["username"]
        password = request.form["password"]
        message_id = request.form["message_id"]

        try:
            db = sqlite3.connect("database.db")
            query = f"""
            DELETE FROM Forum
            WHERE id = ?
            """
            db.execute(query, (message_id, ))
            db.commit()
            db.close()
            return render_template("delete.html", deleted = True)
        except:
            return render_template("delete.html", deleted = False)

if __name__ == "__main__":
    app.run(debug = True)