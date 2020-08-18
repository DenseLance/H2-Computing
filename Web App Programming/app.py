# HTML/CSS (client side) <--- Python: jinja ---> Python: flask (server side) <--- Python: sqlite 3 ---> DB Browser
# type python in terminal (CTRL + `) to enter python shell
# type exit() to exit python shell
# type pip list to check the libraries that are installed
from flask import Flask

app = Flask(__name__) # __name__ is __main__; uses current file name to create a flask application

@app.route("/") # define behaviour for route directory/url
def home():
    return "My first home page"

if __name__ == "__main__": # if app.py is run, then the application would run
    app.run() # cross-imports would not run the application