from behave import *
from productos import *

@given('{nombre} para listar los productos')
def implemetacion(context, nombre):
    context.productos = Productos()
    context.name = nombre
   
@when('se lista los productos')
def implementacion(context):
    context.list = context.productos.listarNombre(context.name)

@then('el {precio} del producto es correcto')
def implementacion(context, precio):
    print (context.list == precio)