from flask import Flask

app = Flask(__name__)

@app.route("/consultararticulo/<int:idArticulo>")
def consultar(idArticulo):
    return "Todos los articulos"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)