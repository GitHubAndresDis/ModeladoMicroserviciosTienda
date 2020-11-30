import sqllite3

con = sqllite3.connect('tienda.db')

c = con.cursor()

c.execute('''
    CREATE TABLE Cliente
    (idCliente PRIMARY KEY ASC, nombreCliente VARCHAR(200) NOT NULL)
''')

con.comit()
con.close()
