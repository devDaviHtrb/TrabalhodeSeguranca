from flask import Blueprint, jsonify
from myapp.initiDb import db
from sqlalchemy import text

verifyBar = Blueprint("verifyBar", __name__)

@verifyBar.route("/verifyBar/<endereco_filter>", methods=["GET"])
def verify_bar(endereco_filter):
    if not endereco_filter:
        return jsonify({"InputError": "Por favor, coloque o endereço do bar"}), 400
    
    try:
        result = db.session.execute(
            text("CALL query_bar(:enderecoFilter)"),
            {"enderecoFilter": endereco_filter}
        )

        # Converte para lista e pega só o primeiro resultado (se existir)
        row = result.fetchone()
        db.session.close()

        if not row:
            return jsonify({}), 200  # Nenhum bar encontrado

        bar = {
            "reputacao": float(row[0]) if row[0] is not None else None,
            "endereco": row[1],
            "condicao": row[2]
        }

        return jsonify(bar), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
