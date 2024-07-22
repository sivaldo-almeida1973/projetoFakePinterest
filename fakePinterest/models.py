# Importa o banco de dados e o gerenciador de login do módulo fakePinterest
from fakePinterest import database, login_manager
# Importa a classe datetime para manipulação de datas e horas
from datetime import datetime
# Importa UserMixin do Flask-Login para gerenciar a autenticação do usuário
from flask_login import UserMixin

# Função para carregar o usuário pelo ID
@login_manager.user_loader
def load_usuario(id_usuario):
    # Retorna o usuário com o ID fornecido
    return Usuario.query.get(int(id_usuario))

# Define a classe Usuario que representa a tabela de usuários no banco de dados
class Usuario(database.Model, UserMixin):
    # Define a coluna 'id' como chave primária
    id = database.Column(database.Integer, primary_key=True)
    # Define a coluna 'username' como string não nula
    username = database.Column(database.String, nullable=False)
    # Define a coluna 'email' como string não nula e única
    email = database.Column(database.String, nullable=False, unique=True)
    # Define a coluna 'senha' como string não nula
    senha = database.Column(database.String, nullable=False)
    # Define o relacionamento com a tabela 'Foto'
    fotos = database.relationship("Foto", backref="usuario", lazy=True)

# Define a classe Foto que representa a tabela de fotos no banco de dados
class Foto(database.Model):
    # Define a coluna 'id' como chave primária
    id = database.Column(database.Integer, primary_key=True)
    # Define a coluna 'imagem' com um valor padrão
    imagem = database.Column(database.String, default="default.png")
    # Define a coluna 'data_criacao' como datetime não nulo com valor padrão de agora
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now())
    # Define a coluna 'id_usuario' como chave estrangeira referenciando a tabela 'usuario'
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
