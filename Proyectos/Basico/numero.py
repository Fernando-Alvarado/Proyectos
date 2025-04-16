# Proyecto realizado por: [Fernando Alvarado Palacios]
# Fecha: [2025-4-13]
# Descripción del programa:
# Juego para adivinar un número entre 1 y 100. Gana quien lo adivine primero: el jugador o la computadora.

import random 


#Definiendo el constructor del juego
class Juego:
    def __init__(self):
        self.intentos = 0
        self.numero_secreto = random.randint(1, 100)
        self.max= 100
        self.min= 1
        
    def jugador(self, numero):
        if(numero == self.numero_secreto):
            print("Ganaste")
            return 0
        else:
            if numero > self.numero_secreto:
                print("El numero es menor")
            else:
                print("El numero es mayor")
            return 1
                   
    def compu(self):
        numero = random.randint(self.min, self.max)
        if(numero == self.numero_secreto):
            print("La compu gano")
            return 0
        else:
            if numero > self.numero_secreto:
                self.max = numero
            else:
                self.min = numero
            return 1
    
        
        
        

if __name__ == "__main__":
    
    print("En este juego, jugaras un juego de adiviar un numero del 1 al 100 contra la compu, cada uno tendra un turno y quien adivine primero gana")
    juego = Juego()
    salida = 1
    while(salida != 0):
        valor = input("Dame un numero entre 1 y 100: ")
        try:
            valor = int(valor)
            salida = juego.jugador(valor)
            if salida != 0:
                print("La compu esta pensando")
                salida = juego.compu()
            
        except ValueError:
            print("No es un numero")
        
    
    
    
    
    
    



        
        