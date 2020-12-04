from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)

class clientes(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   nit = db.Column(db.String(20))
   nombre = db.Column(db.String(200))

   def __init__(self, nit, nombre):
        self.nit = nit
        self.nombre = nombre


@app.route("/crearcliente/<int:nitCliente>/<string:nombreCliente>")
def crear(nitCliente, nombreCliente):

    cliente = clientes(nitCliente, nombreCliente)

    db.session.add(cliente)
    db.session.commit()

    c = db.session.query(clientes).filter_by(nit=nitCliente).first()
    
    if c is not None:
        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente creado exitosamente',
                                'cliente' : {'nit':c.nit,'nombre':c.nombre},
                                'estadoproceso': 'exitoso',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente no encontrado' ,
                                'estadoproceso': 'fallido',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )

    return response

@app.route("/consultarcliente/<int:nitCliente>")
def consultar(nitCliente):

    c = db.session.query(clientes).filter_by(nit=nitCliente).first()

    if c is not None:
        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente creado exitosamente',
                                'cliente' : {'nit':c.nit,'nombre':c.nombre},
                                'estadoproceso': 'exitoso',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente no encontrado' ,
                                'estadoproceso': 'fallido',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )
    
    return response

@app.route("/modificarcliente/<int:nitCliente>/<string:nombreCliente>")
def modificar(nitCliente, nombreCliente):

    c = db.session.query(clientes).filter_by(nit=nitCliente).first()

    if c is not None:

        c.nombre = nombreCliente
        db.session.commit()

        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente modificado exitosamente' ,
                                'estadoproceso': 'exitoso',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({
                                'mensaje': 'Cliente no encontrado' ,
                                'estadoproceso': 'fallido',
                                'existeError': 'false',
                                'descripcionError':''
                                }),
            mimetype='application/json'
        )

    return response

@app.route("/eliminarcliente/<int:nitCliente>")
def eliminar(nitCliente):

    db.session.query(clientes).filter_by(nit=nitCliente).delete()
    db.session.commit()

    response = app.response_class(
        response=json.dumps({
                            'mensaje': 'Cliente eliminado exitosamente' ,
                            'estadoproceso': 'exitoso',
                            'existeError': 'false',
                            'descripcionError':''
                            }),
        mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0',debug=True)