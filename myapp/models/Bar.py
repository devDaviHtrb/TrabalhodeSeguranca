from myapp.initiDb import db

class bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome =  db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    reputacao = db.Column(db.String(255), nullable=False)
    condicao = db.Column(db.String(255), nullable=False)
