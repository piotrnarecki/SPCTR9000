from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


# komentarz dla zaznaczenia ze to branch Piotra


@app.route("/")
def my_function():
    return render_template("welcome.html",
                           cards=db
                           )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)
