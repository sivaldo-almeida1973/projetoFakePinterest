#criar formulários do site
#pip install flask-wtf
#pip install email-validator

from flask_wtf import FlaskForm  #estrutura da classe
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakePinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmacao de senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario: #se ja existe usuario com este email
            return ValidationError("E-mail já cadastrado, faça login para continuar.")

