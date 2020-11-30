from flask import Flask

app = Flask(__name__)

@app.route("/modificararticulo/<int:idArticulo>/<string:nombreArticulo>/<int:cantidad>")
def crear(idArticulo, nombreArticulo, cantidad):
        return "Articulo modificado correctamente."

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)