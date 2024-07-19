#primeiro importar flask
from flask import Flask, render_template, url_for  #url_for permite alterar rota sem ter problemas
# render_template ,faz carregar os arquivos html, na pasta templates

app = Flask(__name__)

#criar rota(caminho da pagina)da pagina homepage
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

#criar rota(caminho da pagina)da pagina perfil, para qualquer usuario
@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)



#se for importado de outro arquivo, não é para rodar esse codigo
if __name__ == "__main__":
    app.run(debug=True)#qualquer alteração feita , atualiza auto

