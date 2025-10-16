from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from myapp.initiDb import db

from myapp.routes import *
load_dotenv()

app = Flask(__name__, template_folder="myapp/templates", static_folder="myapp/static")
app.secret_key = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

app.register_blueprint(home)
app.register_blueprint(verifyBar)

db.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)