# Funciones
# En este rpoyecto vamos a hacer un juego de black jack 

# Librerias a usar para nuestro proyecto 
import random # Para generar numeros aleatorios




class baraja:
    def __init__(self):
        self.valor = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.palo = ["Corazones", "Diamantes", "Treboles", "Picas*"]
        
    def paquete(self):
        self.cartas = [i  +" de " + j  for i in self.valor for j in self.palo]
        return self.cartas
    
    def barajear(self, numero = 1): # Numero es para saber cuantas barajas vamos a tener 
        self.a = []
        for i in range(numero):
            self.a += self.paquete() #Llamando otro metodoso, para tener nuestro paquete de cartas
        random.shuffle(self.a) # Revolver de manera aleatoria las cartas
        return self.a
        
    





if __name__ == "__main__":
    
    baraja = baraja()
    print(baraja.barajear(2))
    
    print(len(baraja.barajear(2)))
    print("Hola, mundo")