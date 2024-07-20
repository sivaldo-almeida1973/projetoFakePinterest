#primeiro importar flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#cria nosso app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cpmunidade.db"
app.config["SECRET_KEY"] = "3875e5c03b0edef84df63b5844d81ce9"

#cria nosso banco dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"  #direciona


#precisa de routes para funcionar
from fakePinterest import routes_views
