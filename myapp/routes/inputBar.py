from flask import Blueprint,request,  jsonify
from myapp.initiDb import db
from myapp.models import bar
from myapp.initCrypto import fernet

inputBar = Blueprint("inputBar", __name__)

@inputBar.route("/inputBar", methods=["POST"])
def insert_bar():
    nome=request.form.get("nome")
    endereco = request.form.get("endereco")
    status =  request.form.get("condicao")
    reputacao =  request.form.get("reputacao")

    if not (endereco and status and reputacao):
        return jsonify("preencha todos os campos"), 400


    NovoBar = bar(
        nome=nome,
        endereco=fernet.encrypt(endereco.encode()),
        condicao=fernet.encrypt(status.encode()),
        reputacao=fernet.encrypt(reputacao.encode())
    )
    db.session.add(NovoBar)
    db.session.commit()

    return jsonify("bar adicionado com sucesso"), 200