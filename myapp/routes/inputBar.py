from flask import Blueprint, render_template,request, redirect, url_for
from myapp.initiDb import db
from myapp.models import bar
from initCrypto import fernet

verifyBar = Blueprint("verifyBar", __name__)

@verifyBar.route("/inputBar", methods=["GET", "POST"])
@verifyBar.route("/inputBar/<msg>", methods=["GET", "POST"])
def verify_bar(msg=""):
    if request.method == "POST":
        endereco = request.form["endereco"]
        status = request.form["status"]
        reputacao = request.form["reputacao"]
        if endereco and status and reputacao:
            NovoBar = bar(endereco=fernet.encrypt(endereco), status=fernet.encrypt(status), reputacao=fernet.encrypt(reputacao))
            return redirect(url_for("verifyBar", msg = "insert concluido"))
        else:
            return redirect(url_for("verifyBar", msg = "Preencha todos os campos"))
    return render_template("BarForm.html", msg=msg)