from flask import Flask

app = Flask(__name__)

@app.route("/eliminarcliente/<int:idCliente>")
def crear(idCliente):
        return "Cliente eliminado correctamente."

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)