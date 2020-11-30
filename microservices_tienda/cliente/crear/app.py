from flask import Flask
#from qlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.sqlite3'

#db = SQLAlchemy(app)

#class clientes(db.Model):
   #id = db.Column('id', db.Integer, primary_key = True)
   #nit = db.Column(db.String(20))
   #nombre = db.Column(db.String(200))

   #def __init__(self, nit, nombre):
       #self.nit = nit
       #self.nombre = nombre

@app.route("/crearcliente/<int:nitCliente>/<string:nombreCliente>")
def crear(nitCliente, nombreCliente):
        #cliente = clientes(nitCliente, nombreCliente)

         #db.session.add(cliente)
         #db.session.commit()     

         return "Crear cliente OK"   


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)