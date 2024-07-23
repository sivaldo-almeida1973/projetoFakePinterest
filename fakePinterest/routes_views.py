# Importa as funções necessárias do Flask
from flask import render_template, url_for, redirect
# Importa o app, o banco de dados e o bcrypt do módulo fakePinterest
from fakePinterest import app, database, bcrypt
# Importa os modelos de dados Usuario e Foto
from fakePinterest.models import Usuario, Foto
# Importa funções de login do Flask-Login
from flask_login import login_required, login_user, logout_user, current_user
# Importa os formulários de login e criação de conta
from fakePinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename



# Cria a rota para a página inicial (homepage)
@app.route("/", methods=["GET", "POST"])
def homepage():
    # Instancia o formulário de login
    formlogin = FormLogin()
    # Verifica se o formulário foi submetido e é válido
    if formlogin.validate_on_submit():
        # Busca o usuário no banco de dados pelo email
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        # Verifica se o usuário existe e se a senha está correta
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            # Faz o login do usuário
            login_user(usuario)
            # Redireciona para a página de perfil do usuário
            return redirect(url_for("perfil", id_usuario=usuario.id))
    # Renderiza o template da homepage com o formulário de login
    return render_template("homepage.html", form=formlogin)

# Cria a rota para a página de criação de conta
@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    # Instancia o formulário de criação de conta
    formcriarconta = FormCriarConta()
    # Verifica se o formulário foi submetido e é válido
    if formcriarconta.validate_on_submit():
        # Criptografa a senha fornecida pelo usuário
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        # Cria um novo usuário com os dados fornecidos
        usuario = Usuario(username=formcriarconta.username.data,
                          senha=senha,
                          email=formcriarconta.email.data)
        # Adiciona o novo usuário ao banco de dados
        database.session.add(usuario)
        # Confirma a transação no banco de dados
        database.session.commit()
        # Faz o login do novo usuário
        login_user(usuario, remember=True)
        # Redireciona para a página de perfil do usuário
        return redirect(url_for("perfil", id_usuario=usuario.id))
    # Renderiza o template de criação de conta com o formulário
    return render_template("criarconta.html", form=formcriarconta)

# Cria a rota para a página de perfil do usuário
@app.route("/perfil/<id_usuario>", methods=["GET" ,"POST"])
@login_required  # Só permite acesso se o usuário estiver logado
def perfil(id_usuario):
    if int(id_usuario) ==  int(current_user.id):
        #o usuario ta vendo o perfil dele
        form_foto = FormFoto()
        #criar funcionalidade enviar
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            #salvar o arquivo na pasta foto_posts
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            #registrar esse arquivo no banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        # Renderiza o template de perfil com o nome do usuário
        return render_template("perfil.html", usuario=usuario, form=None)

# Cria a rota para a página de logout
@app.route("/logout")
@login_required  # Só permite acesso se o usuário estiver logado
def logout():
    # Faz o logout do usuário
    logout_user()
    # Redireciona para a página inicial (homepage)
    return redirect(url_for("homepage"))
