#criar rotas do nosso site(links)
from flask import render_template, url_for
#import o app que esta dentro do __init__ para poder funcionar
from fakePinterest import app


#criar rota(caminho da pagina)da pagina homepage
@app.route("/")  #url_for permite alterar rota da pagina, sem ter problemas
def homepage():
    return render_template("homepage.html")

#criar rota(caminho da pagina)da pagina perfil, para qualquer usuario
@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
