from flask import Blueprint, render_template

insertPage = Blueprint("insertPage", __name__)

@insertPage.route("/insertPage", methods=["GET", "POST"])
def home_page():
    return render_template("insert.html")