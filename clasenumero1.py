class Coche():
    largo= 200 #creamos los atributos los valores que va a tener esta clase
    ancho= 150
    ruedas= 4
    marcha= False
    motor= 1600

    def arrancar(self): #creamos un metodo
        self.marcha = True #la palabra self hace referencia a los atributos de la clase, fijate en los atributos

    def estadodelvehiculo(self):
        if (self.marcha == True):
                return "El vehiculo esta en marcha"
        else:
                return "El vehiculo esta apagado"

fiat600 = Coche() #instanciar una clase a fiat le digo que se cree en base a coche
#acceder a los atributos
print("el largo del coche es " + str(fiat600.largo)) #agregamos el str si lo concaetnamoscno + fiat600.largo para convertirlo
print("este auto tiene " , fiat600.ruedas) # concatenacion con ,
#acceder al metodo
fiat600.estadodelvehiculo() #preguntamos el estado del vehiculo
fiat600.arrancar() # arrancamos el vehiculo
fiat600.estadodelvehiculo() #volvemos a consultar el estado



#-------------------creamos clase alumnos --------------------

class Alumnos():
        nombre = ""
        edad = 0
        sexo = ""

        def nomb(self, a):
            self.nombre = a
            print(a)
            return a
        
        

        def edada(self, b):
            self.edad = b
            print(b)
            return b


        def sexoa(self, c):
              self.sexo = c
              print(c)
              return c


gaston = Alumnos()
print()
gaston.nomb("gaston")
gaston.edada(18)
gaston.sexoa("masculino")

print()

lucas = Alumnos()
print()
lucas.nomb("lucas")
lucas.edada(18)
lucas.sexoa("masculino")
print()
