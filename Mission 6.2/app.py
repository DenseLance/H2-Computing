from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

db = sqlite3.connect("Anime Recommendation.db")
db.close()

## Dataset:
## https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews

@app.route("/")
def home():
    db = sqlite3.connect("Anime Recommendation.db")
    query = """
            SELECT User.Username, Anime.Name, Recommendation.Date, Recommendation.Rating, Recommendation.SimilarAnime, Recommendation.Comment, Recommendation.AnimeID
            FROM User, Anime, Recommendation
            WHERE Recommendation.UserID = User.UserID
            AND Recommendation.AnimeID = Anime.AnimeID
            ORDER BY Recommendation.Date DESC
            """
    cursor = db.execute(query)
    data = cursor.fetchall()
    cursor.close()

    dates = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    query = """
            SELECT Name
            FROM Anime
            WHERE AnimeID = ?
            """
    for row_index in range(len(data)):
        data[row_index] = list(data[row_index])
        data[row_index].append(data[row_index][4])
        data[row_index][2] = str(int(data[row_index][2][-2:])) + " " + dates[int(data[row_index][2][4:6]) - 1] + " " + data[row_index][2][0:4]
        cursor = db.execute(query, (data[row_index][4], ))
        data[row_index][4] = cursor.fetchone()[0]
        data[row_index][5] = repr(data[row_index][5]).replace("\\'", "'")
        data[row_index][5] = str(data[row_index][5][1:].replace("\\r\\n", "<br />"))[:-1]
        cursor.close()
    
    db.close()
    return render_template("home.html", data = data)

@app.route("/index/")
@app.route("/home/")
def index():
    return redirect(url_for("home"))

@app.route("/search/", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        db = sqlite3.connect("Anime Recommendation.db")
        query = """
                SELECT AnimeID, Name
                FROM Anime
                WHERE Name LIKE ?
                """
        cursor = db.execute(query, ("%" + request.form["anime"] + "%", ))
        data = cursor.fetchall()

        if len(data) == 0:
            return redirect(url_for("search"))
        elif len(data) == 1:
            return redirect(url_for("result", animeid = data[0][0]))
        else:
            return render_template("search.html", data = data)

@app.route("/<animeid>")
def result(animeid):
    db = sqlite3.connect("Anime Recommendation.db")
    query = """
            SELECT *
            FROM Anime
            WHERE AnimeID = ?
            """
    cursor = db.execute(query, (animeid, ))
    anime = list(cursor.fetchone())
    
    dates = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if anime[2] != None:
        anime[2] = str(int(anime[2][-2:])) + " " + dates[int(anime[2][4:6]) - 1] + " " + anime[2][0:4]
    else:
        anime[2] = "-"
    if anime[3] != None:
        anime[3] = str(int(anime[3][-2:])) + " " + dates[int(anime[3][4:6]) - 1] + " " + anime[3][0:4]
    else:
        anime[3] = "-"
    cursor.close()

    query = """
            SELECT Genre
            FROM AnimeGenre
            WHERE AnimeID = ?
            """
    cursor = db.execute(query, (animeid, ))
    genre_tup = cursor.fetchall()
    genre_list = []

    for tup in genre_tup:
        genre_list.append(tup[0])

    genre = ", ".join(genre_list)
        
    cursor.close()
    
    query = """
            SELECT User.Username, Anime.Name, Recommendation.Date, Recommendation.Rating, Recommendation.SimilarAnime, Recommendation.Comment, Recommendation.AnimeID
            FROM User, Anime, Recommendation
            WHERE Recommendation.UserID = User.UserID
            AND Recommendation.AnimeID = Anime.AnimeID
            AND Anime.AnimeID = ?
            ORDER BY Recommendation.Date DESC
            """
    cursor = db.execute(query, (animeid, ))
    data = cursor.fetchall()
    cursor.close()

    query = """
            SELECT Name
            FROM Anime
            WHERE AnimeID = ?
            """
    # try-except
    for row_index in range(len(data)):
        data[row_index] = list(data[row_index])
        data[row_index].append(data[row_index][4])
        data[row_index][2] = str(int(data[row_index][2][-2:])) + " " + dates[int(data[row_index][2][4:6]) - 1] + " " + data[row_index][2][0:4]
        cursor = db.execute(query, (data[row_index][4], ))
        data[row_index][4] = cursor.fetchone()[0]
        data[row_index][5] = repr(data[row_index][5]).replace("\\'", "'")
        data[row_index][5] = str(data[row_index][5][1:].replace("\\r\\n", "<br />"))[:-1]
        cursor.close()
    
    db.close()
    return render_template("result.html", anime = anime, genre = genre, data = data)

@app.route("/recommend/", methods = ["GET", "POST"])
def recommend():
    if request.method == "GET":
        return render_template("recommend.html")
    else:
        username = request.form["username"] # select
        anime = request.form["anime"] # select
        date = str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(datetime.datetime.now().day)
        rating = request.form["rating"]
        comment = request.form["comment"]
        similar_anime = request.form["similar_anime"] # select

        db = sqlite3.connect("Anime Recommendation.db")
        
        # userid
        query = """
                SELECT UserID
                FROM User
                WHERE Username = ?
                """
        cursor = db.execute(query, (username, ))
        data = cursor.fetchone()
        if data == None: # username not found
            return redirect(url_for("recommend"))
        else:
            userid = data[0]

        # animeid (anime)
        query = """
                SELECT AnimeID, Name
                FROM Anime
                WHERE Name LIKE ?
                """
        cursor = db.execute(query, ("%" + anime + "%", ))
        data = cursor.fetchall()
        if len(data) == 0: # anime not found
            return redirect(url_for("recommend"))
        elif len(data) == 1: # 1 anime found
            animeid = data[0][0]
            animeid_list = data
        else: # > 1 anime found
            animeid = None
            animeid_list = data

        # animeid (similar anime)
        query = """
                SELECT AnimeID, Name
                FROM Anime
                WHERE Name LIKE ?
                """
        cursor = db.execute(query, ("%" + similar_anime + "%", ))
        data = cursor.fetchall()
        if len(data) == 0: # similar anime not found
            return redirect(url_for("recommend"))
        elif len(data) == 1: # 1 similar anime found
            similar_animeid = data[0][0]
            similar_animeid_list = data
        else: # > 1 similar anime found
            similar_animeid = None
            similar_animeid_list = data
        
        if animeid != None and similar_animeid != None: # found
            try:
                query = """
                        INSERT INTO Recommendation
                        VALUES(?, ?, ?, ?, ?, ?)
                        """
                db.execute(query, (userid, animeid, date, rating, comment, similar_animeid))
                db.commit()
                db.close()
                return redirect(url_for("result", animeid = animeid))
            except sqlite3.IntegrityError:
                return redirect(url_for("recommend"))
        else: # 1 input has more than 1 result
            return render_template("recommend.html",
                                   userid = userid,
                                   animeid_list = animeid_list,
                                   date = date,
                                   rating = rating,
                                   comment = comment,
                                   similar_animeid_list = similar_animeid_list)

@app.route("/sendtodatabase/<userid>/<date>/<rating>/<comment>", methods = ["GET", "POST"])
def sendtodatabase(userid, date, rating, comment):
    if request.method == "GET":
        return redirect(url_for("home"))
    else:
        animeid = request.form["animeid"]
        similar_animeid = request.form["similar_animeid"]

        try:
            db = sqlite3.connect("Anime Recommendation.db")
            query = """
                    INSERT INTO Recommendation
                    VALUES(?, ?, ?, ?, ?, ?)
                    """
            db.execute(query, (userid, animeid, date, rating, comment, similar_animeid))
            db.commit()
            db.close()
            return redirect(url_for("result", animeid = animeid))
        except sqlite3.IntegrityError:
            return redirect(url_for("recommend"))

@app.route("/help/")
def help():
    return render_template("help.html")

if __name__ == "__main__":
    app.run()
