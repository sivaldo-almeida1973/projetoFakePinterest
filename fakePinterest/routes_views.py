#criar rotas do nosso site(links)
from flask import render_template, url_for, redirect
#import o app que esta dentro do __init__ para poder funcionar
from fakePinterest import app
from flask_login import login_required
from fakePinterest.forms import FormLogin, FormCriarConta

#criar rota(caminho da pagina)da pagina homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta",  methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

#criar rota(caminho da pagina) perfil, para qualquer usuario
@app.route("/perfil/<usuario>")
@login_required  #so permite acesso se estiver logado
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
