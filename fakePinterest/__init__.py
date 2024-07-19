#primeiro importar flask
from flask import Flask

#cria nosso app
app = Flask(__name__)

#precisa de routes para funcionar
from fakePinterest import routes_views
