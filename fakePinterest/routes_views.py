#criar rotas do nosso site(links)
from flask import render_template, url_for
#import o app que esta dentro do __init__ para poder funcionar
from fakePinterest import app
from flask_login import login_required

#criar rota(caminho da pagina)da pagina homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

#criar rota(caminho da pagina) perfil, para qualquer usuario
@app.route("/perfil/<usuario>")
@login_required  #so permite acesso se estiver logado
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
