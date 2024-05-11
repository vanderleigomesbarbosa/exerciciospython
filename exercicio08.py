#calcule area de um hexagono regular

import math

lado = float (input("Digite o vaor do lado do hexagono para calcular sua area : "))
resultado=((pow(lado,2)*math.sqrt(3))/2)
print(("area do hexagono é: ",round(resultado,2), " m²"))