# HTML/CSS (client side) <--- Python: jinja ---> Python: flask (server side) <--- Python: sqlite 3 ---> DB Browser
# type python in terminal (CTRL + `) to enter python shell
# type exit() to exit python shell
# type pip list to check the libraries that are installed
from flask import Flask, render_template

app = Flask(__name__) # __name__ is __main__; uses current file name to create a flask application

@app.route("/") # define behaviour for route directory/uri
@app.route("/index/") # add trailing slash is better
def index():
    return render_template("index.html")

@app.route("/about/<name>")
def about(name):
    class_ = "20J13"
    age = 16
    return render_template("about.html", class_ = class_, age = age, name = name)

if __name__ == "__main__": # if app.py is run, then the application would run
    app.run(debug = True) # cross-imports would not run the application
