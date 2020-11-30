from flask import Flask

app = Flask(__name__)

@app.route("/modificarcliente/<int:idCliente>/<string:nombreCliente>")
def crear(idCliente, nombreCliente):
        return "Cliente modificado correctamente."

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)