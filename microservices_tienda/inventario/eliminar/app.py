from flask import Flask

app = Flask(__name__)

@app.route("/eliminararticulo/<int:idArticulo>")
def crear(idArticulo):
        return "Articulo eliminado correctamente."

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)