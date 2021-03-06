# Modelado Arquitectura y Microservicios Tienda

DAINER ANDRES VERGARA RODRGIUEZ
20202099037

RHOSBEN ADHIER CORDOBA AGUILAR 20202099025


  1. Contribución Objetivos
  
  ![Contribución Objetivos](/Modelo%20Arquitectonico/1.%20Contribucion%20Objetivos.PNG) 
  
  
  2. Cooperación de Actores
  
  ![Contribución de Actores](/Modelo%20Arquitectonico/2.%20Cooperacion%20de%20actores.PNG) 
  
  
   3. Cooperación de Procesos de Negocio
  
  ![Contribución de Procesos de Negocio](/Modelo%20Arquitectonico/3.%20Cooperacion%20de%20procesos%20de%20negocio.PNG) 
  
  
   4. Diagrama de la Infraestructura
  
  ![Diagrama de la Infraestructura](/Modelo%20Arquitectonico/4.%20Diagrama%20de%20la%20infraestructura.PNG) 
  
  
  5. Estructura de Aplicaciones
  
  ![Estructura de Aplicaciones](/Modelo%20Arquitectonico/5.%20Estructura%20de%20aplicaciones.PNG) 


  6. Estructura de información
  
  ![Estructura de información](/Modelo%20Arquitectonico/6.%20Estructura%20de%20informacion.PNG) 
  
  
  7. Funciones del negocio
  
  ![Funciones del negocio](/Modelo%20Arquitectonico/7.%20Funciones%20del%20negocio.PNG)
  
  
  8. Motivación
  
  ![Motivación](/Modelo%20Arquitectonico/8.%20Motivacion.PNG)  
  
  
  9. Nivel Aplicación
  
  ![Nivel Aplicación](/Modelo%20Arquitectonico/9.%20Nivel%20aplicacion.PNG)  
  
  
  10. Organización
  
  ![Organización](/Modelo%20Arquitectonico/10.%20Organizacion.PNG)  


  11. Organización e Implementación
  
  ![Organización e Implementación](/Modelo%20Arquitectonico/11.%20Organizacion%20e%20implementacion.PNG) 


  12. Procesos de Negocios
  
  ![Procesos de Negocios](/Modelo%20Arquitectonico/12.%20Procesos%20de%20negocios.PNG) 
  
  
  13. Producto
  
  ![Procesos de Negocios](/Modelo%20Arquitectonico/13.%20Producto.PNG) 
  
  
  14. Realizacion de Requerimientos
  
  ![Procesos de Negocios](/Modelo%20Arquitectonico/14.%20Realizacion%20de%20requerimientos.PNG) 
  
  
  15. Realización del Servicio
  
  ![Realización del Servicio](/Modelo%20Arquitectonico/15.%20Realizacion%20del%20servicio.PNG) 
  
  
  16. Resumen por Capas
  
  ![Resumen por Capas](/Modelo%20Arquitectonico/16.%20Resumen%20por%20capas.PNG)
  
   
   17. Uso de Aplicación
  
  ![Uso de Aplicación](/Modelo%20Arquitectonico/17.%20Uso%20de%20aplicacion.PNG)
  
  
  18. Uso de Infraestructura
  
  ![Uso de Infraestructura](/Modelo%20Arquitectonico/18.%20Uso%20de%20infraestructura.PNG)



# Test consumo Microservicios - Tienda

  1. Creación de un cliente.
  
   http://localhost:8080/crearcliente/2/Rhosben
     
     Ejemplo de posible resultado esperado
     
     { 
        "cliente": {
                    "nit": "2", 
                    "nombre": "Rhosben"
                    }, 
        "descripcionError": "", 
        "estadoproceso": "exitoso", 
        "existeError": "false", 
        "mensaje": "Cliente creado exitosamente"
      }


2. Consulta de un cliente.

  http://localhost:8080/consultarcliente/1
    
    Ejemplo de posible resultado esperado
      
    {
      "descripcionError": "", 
      "estadoproceso": "fallido", 
      "existeError": "false", 
      "mensaje": "Cliente no encontrado"
    }


3. Modificación de un cliente.

  http://localhost:8080/modificarcliente/1/Andres
  
    Ejemplo de posible resultado esperado
    
    {
      "descripcionError": "", 
      "estadoproceso": "fallido", 
      "existeError": "false", 
      "mensaje": "Cliente no encontrado"
    }
    
    
4. Eliminación de un cliente.

 http://localhost:8080/eliminarcliente/1

    Ejemplo de posible resultado esperado

    {
      "descripcionError": "", 
      "estadoproceso": "exitoso", 
      "existeError": "false", 
      "mensaje": "Cliente eliminado exitosamente"
    }
    
    
5. Creación de un articulo.
    
  http://localhost:8080/creararticulo/1/Computadora/4
  
    Ejemplo de posible resultado esperado

    {
      "articulo": {
                    "cantidad": 4, 
                    "codigo": "1", 
                    "nombre": "Computadora"
                  }, 
      "descripcionError": "", 
      "estadoproceso": "exitoso", 
      "existeError": "false", 
      "mensaje": "Articulo creado exitosamente"
    }


6. Consulta de un articulo.

  http://localhost:8080/consultararticulo/1

    Ejemplo de posible resultado esperado
  
    { 
      "descripcionError": "", 
      "estadoproceso": "fallido", 
      "existeError": "false", 
      "mensaje": "Articulo no encontrado"
    }
  

7. Modificación de un articulo.

  http://localhost:8080/modificararticulo/1/Computadora/4
  
    Ejemplo de posible resultado esperado
    
    { 
      "descripcionError": "", 
      "estadoproceso": "fallido", 
      "existeError": "false", 
      "mensaje": "Articulo no encontrado"
    }
    

8. Eliminación de un articulo.

  http://localhost:8080/eliminararticulo/1
  
    Ejemplo de posible resultado esperado
    
    { 
      "descripcionError": "", 
      "estadoproceso": "exitoso", 
      "existeError": "false", 
      "mensaje": "Articulo eliminado exitosamente"
    }
  
  
  
# Evidencias pruebas

 ![Imagen](/Modelo%20Arquitectonico/WhatsApp%20Image%202020-12-04%20at%2013.20.33.jpeg)
 
 ![Imagen](/Modelo%20Arquitectonico/WhatsApp%20Image%202020-12-04%20at%2013.20.55.jpeg)
 
 ![Imagen](/Modelo%20Arquitectonico/WhatsApp%20Image%202020-12-04%20at%2013.21.21.jpeg)
 
 ![Imagen](/Modelo%20Arquitectonico/WhatsApp%20Image%202020-12-04%20at%2013.21.41.jpeg)







