from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articulos.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)

class articulos(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   codigo = db.Column(db.String(20))
   nombre = db.Column(db.String(200))
   cantidad = db.Column(db.Integer)

   def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

@app.route("/creararticulo/<int:codigoArticulo>/<string:nombreArticulo>/<int:cantidad>")
def crear(codigoArticulo, nombreArticulo, cantidad):

        articulo = articulos(codigoArticulo, nombreArticulo, cantidad)

        db.session.add(articulo)
        db.session.commit()

        c = db.session.query(articulos).filter_by(codigo=codigoArticulo).first()
        
        if c is not None:
                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo creado exitosamente',
                                        'articulo': {'codigo':c.codigo,'nombre':c.nombre, 'cantidad':c.cantidad},
                                        'estadoproceso': 'exitoso',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )
        else:
                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo no encontrado' ,
                                        'estadoproceso': 'fallido',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )

        return response
        

@app.route("/consultararticulo/<int:codigoArticulo>")
def consultar(codigoArticulo):
        
        c = db.session.query(articulos).filter_by(codigo=codigoArticulo).first()

        if c is not None:
                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo creado exitosamente',
                                        'articulo': {'codigo':c.codigo,'nombre':c.nombre, 'cantidad':c.cantidad},
                                        'estadoproceso': 'exitoso',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )
        else:
                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo no encontrado' ,
                                        'estadoproceso': 'fallido',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )
        
        return response

@app.route("/modificararticulo/<int:codigoArticulo>/<string:nombreArticulo>/<int:cantidad>")
def modificar(codigoArticulo, nombreArticulo, cantidad):
        c = db.session.query(articulos).filter_by(codigo=codigoArticulo).first()

        if c is not None:

                c.nombre = nombreArticulo
                c.cantidad = cantidad
                db.session.commit()

                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo modificado exitosamente' ,
                                        'estadoproceso': 'exitoso',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )
        else:
                response = app.response_class(
                response=json.dumps({
                                        'mensaje': 'Articulo no encontrado' ,
                                        'estadoproceso': 'fallido',
                                        'existeError': 'false',
                                        'descripcionError':''
                                        }),
                mimetype='application/json'
                )

        return response

@app.route("/eliminararticulo/<int:codigoArticulo>")
def eliminar(codigoArticulo):
        db.session.query(articulos).filter_by(codigo=codigoArticulo).delete()
        db.session.commit()

        response = app.response_class(
        response=json.dumps({
                            'mensaje': 'Articulo eliminado exitosamente' ,
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