#valor = int(input("Coloque su valor aquí: "))
#valorMinimo = 0
#valorMaximo = 5
#dentroDeRango = valor >= valorMinimo and valor <= valorMaximo
#if dentroDeRango:
#    print(f"El número {valor} está dentro de rango")
#else:
#    print(f"El número {valor} está fuera de rango")

#vacaciones = False
#diaLibre = False
#if not (vacaciones or diaLibre):
 #   print("NO Puedo ir a tu juego")
#else:
 #   print("puede ir a tu juego")

#print("Proporcione los datos del libro: ")
#nombre = input("Proporcione nombre del libro: ")
#id = int(input("Proporcione id del libro: "))
#precio = float(input("Proporcione precio del libro:" ))
#envioGratuito = (input("Indica si es envío gratuito (True) or (False): "))
#
#if envioGratuito == "True":
 #   envioGratuito = True
#elif envioGratuito == "False":
 #   envioGratuito = False
#else:
#    print("Error, coloque un valor True o False")

#numero = int(input("Escriba un Número: "))
#numeroTexto = ""
#if numero == 1:
    #numeroTexto = "Número uno"
#elif numero == 2:
    #numeroTexto = "Número dos"
#else:
   # numero = "Fuera de Rango"
#print(f"Número Proporcionado: {numero} - {numeroTexto} ")

#contador = 0
#while contador < 3:
    #print(contador)
    #contador += 1
#else:
  #  print("Fin del ciclo")
#nombres = ["Marcos","Lautaro","Camila"]
#notas = [5,7,8]
#nombre = (input("Coloque numero del alumno: "))
#print(nombre)


#for i in range(10):
   # if i %3 == 0:
      #  print(i)
#tupla = (13, 1, 8, 3, 2, 5, 8)
#lista = []
#for elemento in tupla:
   # if elemento < 5:
     #   lista.append(elemento)

#print(lista)

#def sumar(a, b):
    #return a + b
#resultado = sumar(5, 3)

#print(f"El resultado de la suma es: {sumar(5, 3)}")

#def listadeNombres(*args):
 #   for name in args:
   #     print(name)
#
#listadeNombres("Juan","Pedro","Nicolás")

#def suma (*args):
    #return args
#definirArgs = (50 + 17 + 18)
#print(suma(definirArgs))

#Definición de la función para sumar valores
#def sumar_valores(*args):
    #resultado = 0
    #for valor in args:
        #resultado += valor
    #return resultado

#LLamada de la función
#print(sumar_valores(3,5,9))

#def multiplicar_valores(*numeros):
    #resultado = 1
   # for numero in numeros:
   #     resultado *= numero
   # return resultado
#print(multiplicar_valores(3,5,15))

#def divide(*args):
    #result = 1
    #for number in args:
     #   result /= numero
    #return result
#print(divide(4/5/8))

#def dividir_valores(*numeros):
    #resultado = 1
    #for numero in numeros:
       # resultado /= numero
   # return resultado
#print(dividir_valores(3,5,15))
#def dividirValores(*args):
    #result = 1
    #for number in args:
        #result /= number
    #return result


#print(int(dividirValores(1)))
#def multiply_values(*args) -> int:
   # result = 1
    #for n in args:
       # if isinstance(n, int):
           # result = result * n
    #return result


#print(multiply_values(5, 6, -13, -20, '10000000'))
#def listarTerminos(**terminos):
    #for llave, valor in terminos.items():
        #print(f"{llave}: {valor} ")
#listarTerminos(IDE="Integrated development Environment")

#def desplegarNombres(nombres):DECLARANDO FUNCION
  #  for nombre in nombres:
   #     print(nombres)

#nombres = ["Marta", "Luisa", "Benita"] DECLARANDO VARIABLES
#desplegarNombres(nombres) #LLAMANDO FUNCION

#def factorial(numero):
    #if numero == 1:
    #    return 1
    #else:
        #return numero * factorial(numero-1)
#resultado = factorial(5)
#print(f"El factorial de 5 es: {resultado}")


#def numeroRecursivo(numero):
    #if numero >= 1:
        #print(numero)
        #numeroRecursivo(numero-1)

#print(numeroRecursivo(10))

#def compra(dinero):
    #impuestos = dinero * 10 /100
    #if dinero >0:
        #return dinero + impuestos
#print(compra(100))

#def calcularTotal (pagosinimpuestos, impuestos):
    #return pagosinimpuestos*(impuestos/100)
#pagosinimpuestos = float(input("Escriba pago sin impuestos: "))
#impuestos = float(input("Escriba cantidad de impuestos: "))
#pagoconimpuesto = calcularTotal(pagosinimpuestos, impuestos)
#print(f"Su Pago total es de: ", {pagoconimpuesto})

#def convertirGrados(celcius, farenheit):
#    return celcius * farenheit
#celcius = float(input("Inserte cantidad de grados C°: "))
#farenheit = celcius*1.8000 +32.00
#sumaDeGrados = convertirGrados(celcius, farenheit)
#print(f"La cantidad de grados es: ", {sumaDeGrados})

#ef convertirGrados(farenheit, celcius):
 #   return farenheit / celcius
#celcius = farenheit/1.8000 +32.00
#farenheit = float(input("Escriba la cantidad de grados farenheit: "))
#sumaDeGrados = convertirGrados(farenheit, celcius)
#print(f"La cantidad de grados es: ", {sumaDeGrados})

# Función que convierte de celsius a fahrenheit
#def celsius_fahrenheit(celsius):
        #return celsius * 9/5 + 32

#def fahrenheit_celsius(fahrenheit):
        #return (fahrenheit-32) * 5/9

# Función que convierte de celsius a fahrenheit
###def celsius_fahrenheit(celsius):
        ###return celsius * 9/5 + 32

###def fahrenheit_celsius(fahrenheit):
        ###return (fahrenheit-32) * 5/9

# Realizamos algunas pruebas de conversión
###celsius = float(input('Proporcione su valor en celsius: '))
#resultado = celsius_fahrenheit(celsius)
# Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
#print(f'{celsius} C a F: {resultado:.2f}')
#fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
#resultado = fahrenheit_celsius(fahrenheit)
#print(f'{fahrenheit} F a C: {resultado:.2f}')


#def celsius_fahrenheit(celsius):
    #return (celsius * 1.8) + 32


#def fahrenheit_celsius(fahrenheit):
   # return (fahrenheit-32) * 5/9


#x = celsius_fahrenheit(float(input('Ingresar la temperatura en grados centigrados:')))
#y = fahrenheit_celsius(float(input('Ingresar la temperatura en grados Fahrenheit:')))
#print(f'La temperatura en °C transformada en °F es: {x}')
#print(f'La temperatura en °F transformada en °C es: {y}')
'''
class Persona:
    def __init__(self,nombre,apellido,edad, *args, **kwargs):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._args = args
        self._kwargs = kwargs
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def  edad(self):
        return self._edad

    @apellido.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(selfself, nombre):
        self._nombre = nombre

        #PARA ENCAPSULAR _ "GUIÓN BAJO"

    def mostrarDetalles(self):
           print(f"Persona: {self._nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}")

persona1 = Persona("Juan","Pérez",28, 33253,2,3,5, m = "manzana", p = "pera")
persona1.nombre = "Cambio"
print(persona1._nombre)
'''



# GET = RECUPERAR/OBETENER ATRIBUTOS SET = COLOCAR/MODIFICAR


#class Aritmetica:
   # def __init__(self, operandoA, operandoB):
   #     self.operandoA = operandoA
  #      self.operandoB = operandoB

 #   def sumar(self):
#        return self.operandoA + self.operandoB

    #def restar(self):
     #   return self.operandoA - self.operandoB

    #def multiplicar(self):
   #     return self.operandoA * self.operandoB

  #  def dividir(self):
 #       return self.operandoA / self.operandoB

#aritmetica1 = Aritmetica(5,10)
#print(f"Resultado de suma: ",{aritmetica1.sumar()})
#print(f"Resultado de resta: ",{aritmetica1.restar()})
#print(f"Resultado de multiplicación: ",{aritmetica1.multiplicar()})
#print(f"Resultado de división: ",{aritmetica1.dividir()})

#class Rectangulo:
   # def __init__(self, altura, base):
        #self.altura = altura
        #self.base = base

    #def calcularArea(self):
       # return  self.altura * self.base

#altura = int(input("Coloque altura: "))
#base = int(input("Coloque base: "))
#rectangulo1 = Rectangulo(base, altura)
#print(f"Área: ", {rectangulo1.calcularArea()})


#class Cubo:
    #def __init__(self, ancho, alto, profundidad):
     #   self.ancho = ancho
    #    self.alto = alto
   #     self.profundidad = profundidad

  #  def caclcularCubo(self):
 #       return self.ancho * self.alto  * self.profundidad

#ancho = int(input("Ingrese ancho: "))
#altura = int(input("Ingrese altura: "))
#profundidad = int(input("Ingrese profundidad: "))
#cubo1 = Cubo(ancho, altura, profundidad)

#print(cubo1.caclcularCubo())




'''
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas) ##IMPORTANTANTE
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo


vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

coche = Coche("Azul", 4, 150)
print(coche)

bicicleta = Bicicleta("Blanca", 2, "Urbana")
print(bicicleta)
'''

'''
class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    def infoPersonal(self):
        print(f"EL nombre de la persona es: {self.nombre}\n El apellido es: {self.apellido}\n Su edad es: {self.edad}\n Su sexo es {self.sexo}")
persona1 = Persona("Juan","Gómez",20,"masculino")
print(persona1.infoPersonal())
'''

'''
class Coche:
    def __init__(self, color, kilometros, año):
        self.color = color
        self.kilometros = kilometros
        self.año = año
    def __str__(self):
        return f"Se ha creado un auto de color {self.color}, con {self.kilometros} kilómetros, año {self.año}."
coche1 = Coche("Rojo", 200.000, 2011)

class Bicicleta(Coche):
    def __init__(self, color, kilometros, año,tipoDeBici):
        super().__init__(color, kilometros, año)
        self.tipoDeBici = tipoDeBici

    def __str__(self):

        return f"Su bicicleta es de color {self.color}, con {self.kilometros} kilómetros, año {self.año}. {super().__str__()}"

#Ejemplo de polimorfismo

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))

bicicleta1 = Bicicleta("Rojo", 15, 2000, "mountain bike")

imprimir_detalles(coche1)
'''
