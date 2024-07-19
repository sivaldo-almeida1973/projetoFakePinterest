#primeiro importar flask
from flask import Flask, render_template
# render_template ,faz carregar os arquivos html, na pasta templates

app = Flask(__name__)

#criar rota(caminho da pagina)da pagina homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

#criar rota(caminho da pagina)da pagina perfil
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")



#se for importado de outro arquivo, não é para rodar esse codigo
if __name__ == "__main__":
    app.run(debug=True)#qualquer alteração feita , atualiza auto

