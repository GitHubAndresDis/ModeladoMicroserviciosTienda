from flask import Flask

app = Flask(__name__)

@app.route("/consultarcliente/<int:idCliente>")
def consultar(idCliente):
    return "Todos los clientes"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)