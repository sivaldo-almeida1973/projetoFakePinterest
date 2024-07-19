#primeiro importar flask
from flask import Flask

app = Flask(__name__)

#criar rota(caminho do site)
@app.route("/")
def homepage():
    return "fakePinterest - Meu primeiro site no ar"

#se for importado de outro arquivo, não é para rodar esse codigo
if __name__ == "__main__":
    app.run(debug=True)#qualquer alteração feita , atualiza auto

