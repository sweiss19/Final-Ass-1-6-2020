from app import app
from flask import render_template


# If a user tries to access either no page# (e.g. www.touro.edu/)
# or the index page, then call index()
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home Page")


@app.route('/poems')
def poems():
    return render_template('poem_titles.html', title="Poems")


@app.route('/chess')
def chess():
    return render_template('chess.html', title="Chess")
