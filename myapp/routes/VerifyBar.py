from flask import Blueprint, jsonify
from myapp.initiDb import db
from myapp.models import bar
from myapp.initCrypto import fernet

verifyBar = Blueprint("verifyBar", __name__)

@verifyBar.route("/verifyBar/<nome>", methods=["GET"])
def verify_bar(nome):
    if not nome:
        return jsonify({"InputError": "Por favor, coloque o nome do bar"}), 400
    try:
        barPesquisado = bar.query.filter_by(nome = str(nome)).first()
        if barPesquisado:
            barDescriptografado = {"nome":barPesquisado.nome, "endereco": fernet.decrypt(barPesquisado.endereco.encode()).decode(), "reputacao": float(fernet.decrypt(barPesquisado.reputacao.encode()).decode()), "status": fernet.decrypt(barPesquisado.condicao.encode()).decode()}
            #o fernet só aceita byte, por o encode() dps pra usar os dados é usar o decode
            return jsonify(barDescriptografado), 200
        else:
            return jsonify({}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
