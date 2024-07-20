#criar estrtutura do banco de dados
# pip install flask-sqlalchemy
from fakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin #diz qual classe ira gerenciar login(Usuario

@login_manager.user_loader
def load_usuario(id_usuario):
     return Usuario.query.get(int(id_usuario))

 #criar tabelas
class Usuario(database.Model, UserMixin):
     id =  database.Column(database.Integer, primary_key=True)
     username = database.Column(database.String, nullable=False)
     email =   database.Column(database.String, nullable=False, unique=True)
     senha =  database.Column(database.String, nullable=False)
     fotos =  database.relationship("Foto", backref="usuario", lazy=True)



class Foto(database.Model):
     id = database.Column(database.Integer, primary_key=True)
     imagem = database.Column(database.String, default="default.png")
     data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now())
     id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id') ,nullable=False)    #relacao de foto com usuario
