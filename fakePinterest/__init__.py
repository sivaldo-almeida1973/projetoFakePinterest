#primeiro importar flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

#cria nosso app
app = Flask(__name__)
# if os.getenv('DEBUG') == 0:
#     link_banco = os.getenv("DATABASE_URL")
# else:
#     link_banco = "sqlite://comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "jdbc:postgresql://dpg-cqi2qrggph6c73ealk20-a.oregon-postgres.render.com/banco_sivaldo?user=banco_sivaldo_user&password=oPAjMENGSHfx1W2LuRf8PxlapH3yDPlu"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "3875e5c03b0edef84df63b5844d81ce9"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"


#cria nosso banco dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"  #direciona


#precisa de routes para funcionar
from fakePinterest import routes_views
