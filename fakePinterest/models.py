#criar estrtutura do banco de dados
# pip install flask-sqlalchemy
from fakePinterest import database
from datetime import datetime

 #criar tabelas
class Usuario(database.Model):
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
