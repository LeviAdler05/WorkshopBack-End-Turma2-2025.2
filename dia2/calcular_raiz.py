#Calcula a raiz quadrada de um número fornecido pelo usuário


import math

def calcular_raiz_quadrada(numero):
	return math.sqrt(numero)

num = float(input("Digite um número: "))
raiz = calcular_raiz_quadrada(num)
print(f"A raiz quadrada de {num} é {raiz}")

