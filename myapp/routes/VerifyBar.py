from flask import Blueprint, jsonify
from myapp.initiDb import db
from myapp.models import bar
from initCrypto import fernet

verifyBar = Blueprint("verifyBar", __name__)

@verifyBar.route("/verifyBar/<endereco_filter>", methods=["GET"])
def verify_bar(endereco_filter):
    if not endereco_filter:
        return jsonify({"InputError": "Por favor, coloque o endereço do bar"}), 400
    
    try:
        barPesquisado = bar.query.filter_by(enderenco = fernet.encrypt(endereco_filter)).first()
        if barPesquisado:
            barDescriptografado = {"endereço": fernet.decrypt(barPesquisado.endereco), "reputação": float(fernet.decrypt(barPesquisado.reputacao)), "status": fernet.decrypt(barPesquisado.condicao)}
            return jsonify(barDescriptografado), 200
        else:
            return jsonify({}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
