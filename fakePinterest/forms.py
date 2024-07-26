# Importa a classe FlaskForm do Flask-WTF para criar formulários
from flask_wtf import FlaskForm
# Importa os campos de formulário do WTForms
from wtforms import StringField, PasswordField, SubmitField, FileField
# Importa os validadores do WTForms
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
# Importa o modelo Usuario do módulo fakePinterest
from fakePinterest.models import Usuario

# Define a classe FormLogin que herda de FlaskForm
class FormLogin(FlaskForm):
    # Campo de e-mail com validadores de presença e formato de e-mail
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    # Campo de senha com validador de presença
    senha = PasswordField("Senha", validators=[DataRequired()])
    # Botão de submissão do formulário
    botao_confirmacao = SubmitField("Fazer Login")

      # Método para validar se o e-mail já está cadastrado
    def validate_email(self, email):
        # Busca um usuário no banco de dados com o e-mail fornecido
        usuario = Usuario.query.filter_by(email=email.data).first()
        # Se o usuário já existe, lança um erro de validação
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta!")


# Define a classe FormCriarConta que herda de FlaskForm
class FormCriarConta(FlaskForm):
    # Campo de e-mail com validadores de presença e formato de e-mail
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    # Campo de nome de usuário com validador de presença
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    # Campo de senha com validadores de presença e comprimento mínimo e máximo
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    # Campo de confirmação de senha com validadores de presença e igualdade com o campo de senha
    confirmacao_senha = PasswordField("Confirmacao de senha", validators=[DataRequired(), EqualTo("senha")])
    # Botão de submissão do formulário
    botao_confirmacao = SubmitField("Criar Conta")

    # Método para validar se o e-mail já está cadastrado
    def validate_email(self, email):
        # Busca um usuário no banco de dados com o e-mail fornecido
        usuario = Usuario.query.filter_by(email=email.data).first()
        # Se o usuário já existe, lança um erro de validação
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")

#formulario de enviar foto---(FileField) ,
# para esse formulario ser usado , tem que ser
# importado la no routes_views.py/perfil
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
