#primeiro importar flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#cria nosso app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cpmunidade.db"

database = SQLAlchemy(app)


#precisa de routes para funcionar
from fakePinterest import routes_views
