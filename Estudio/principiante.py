a = 10

print(a)


#1. Crea una variable `altura` con tu estatura en metros y verifica que sea tipo `float`.
#2. Usa una cadena de texto para crear un saludo personalizado, concatenando variables.
#3. Verifica si un número es par y guarda el resultado en una variable booleana.

#Ejercicio 1
altura = 1.75
print(type(altura))

#Ejercicio 2
nombre = "Juan"
apellido = "Pérez"
saludo = "Hola, mi nombre es " + nombre + " " + apellido
print(saludo)

#Ejercicio 3
numero1 = 4
numero2 = 5

es_par = numero1 % 2 == 0
print(es_par)


#1. Escribe un programa que pida un número y diga si es positivo, negativo o cero.
#2. Imprime los números del 1 al 10 usando un `for`.
#3. Suma los números del 1 al 100 usando un `while`.
#4. Escribe un bucle que recorra una lista de nombres y se detenga si encuentra `"Pedro"`.
#5. Imprime solo los números impares entre 1 y 20 (usa `continue`).

respuesta1 = input("Introduce un número: ")
numero = int(respuesta1)

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
   
#Ejercicio 5 
for i in range(1, 21):
    if i % 2 == 0:
        continue
    #print(i)
    

i = 1
contador = 0

while i <= 100:
    contador += i
    i += 1
    
print("La suma de los números del 1 al 100 es:", contador)



#1. Escribe una función que reciba dos números y retorne su división. Si el divisor es cero, captura el error e imprime un mensaje.
#2. Intenta convertir una cadena `"abc"` a entero usando `int()`. Captura el error y muestra qué tipo de error fue.
#3. Usa un bloque `try/except/finally` para abrir un archivo ficticio (`"no_existe.txt"`), capturar el error y escribir un mensaje en `finally`.
#4. Crea una función que pida al usuario su edad (con `input()`), convierta a entero y maneje si la entrada no es válida.

#Ejecicio 1

def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


division(10,0)
division(4,6)

#Ejercicio 2
def suma(a,b):
    try:
        return a + b
    except TypeError:
        print("No se puede sumar un número y una cadena")
        
suma(10, "a")

