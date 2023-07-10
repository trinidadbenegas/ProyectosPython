import mysql.connector


class Conectar:
    def __init__(self):
        try:
            self.conexion= mysql.connector.connect(
                host=  'localhost',
                port= 3306,
                user='root',
                password='',
                db='cliente'

            )
            if self.conexion.is_connected:
                print("se conecto")

        except mysql.connector.Error as descriptionError:
            print("No se conecto", descriptionError)

#PRIMERA OPERACION CRUD - CREAR
    def InsertarValor (self,codigo,nombre,apellido):
        if self.conexion.is_connected(): #primero verificar si hay conexion con la base de datos
            try:
            #crear una variable cursor es muy importante
                cursor= self.conexion.cursor() #permite ejecutar sentencias sql desde python
                sentencia="INSERT INTO clientes VALUES(%s,%s,%s)"
                data= (codigo,nombre,apellido)#datos que recibimos por teclado
                cursor.execute(sentencia, data)
                self.conexion.commit() #comitear los datos
                self.conexion.close() #siempre cerrar la conexion
            except:
                print("No se pudo conectar a la bd")
 # SEGUNDO CRUD- LEER   
    def BuscarObjeto(self):
        if self.conexion.is_connected(): #primero verificar si hay conexion con la base de datos
            try:
            #crear una variable cursor es muy importante
                cursor= self.conexion.cursor() #permite ejecutar sentencias sql desde python
                sentencia="SELECT * FROM clientes"
                cursor.execute(sentencia) #esta sentencia trae datos que hay q almacenar en una varaible
                resultadoConsulta= cursor.fetchall() #trae los datos de la consulta y lo guardamos en una variable
                self.conexion.close() #siempre cerrar la conexion
                return resultadoConsulta
            except:
                print("No se pudo conectar")

#CUARTO CRUD BORRAR

    def EliminarObjeto (self, codigo):
        if self.conexion.is_connected(): #primero verificar si hay conexion con la base de datos
            try:
            #crear una variable cursor es muy importante
                cursor= self.conexion.cursor() #permite ejecutar sentencias sql desde python
                sentencia="DELETE FROM Clientes WHERE Codigo = codigo"
                cursor.execute(sentencia)
                #si hago un rollback estoy a tiempo de que no se borren los datos si me olvide el WHERE
                self.conexion.commit() #comitear los datos
                self.conexion.close() #siempre cerrar la conexion
            except:
                print("No se pudo conectar")


EliminarRegistro= Conectar()
EliminarRegistro.EliminarObjeto(3)



dni=int(input("escriba dni: "))
nombre=input("escriba nombre: ")
apellido=input("escriba apellido: ")
telefono= int(input("escriba telefono: "))
direccion= input("escriba direccion: ")
NuevoRegistro= Conectar()
CrearObjeto= NuevoRegistro.InsertarValor(dni,nombre,apellido,telefono,direccion)

