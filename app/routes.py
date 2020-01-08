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


@app.route('/grey')
def grey():
    return render_template('cold_and_grey.html', title="Cold and Grey")


@app.route('/imprisoned')
def imprisoned():
    return render_template('imprisoned.html', title="Imprisoned")


@app.route('/journey')
def journey():
    return render_template('a_journey.html', title="A Journey")


@app.route('/letting')
def letting():
    return render_template('letting_go.html', title="Letting Go")


@app.route('/seal')
def seal():
    return render_template('navy_seal.html', title="Navy Seal")

