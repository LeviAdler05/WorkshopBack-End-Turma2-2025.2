# Calcula o piso, teto e arredondamento de um número real fornecido pelo usuário

import math

def arredondar_piso(numero):
	return math.floor(numero)

def arredondar_teto(numero):
	return math.ceil(numero)

def arredondar_mais_proximo(numero):
	return round(numero)

num = float(input("Digite um número real: "))

piso = arredondar_piso(num)
teto = arredondar_teto(num)
mais_proximo = arredondar_mais_proximo(num)

print(f"Valor original: {num}")
print(f"Piso (para baixo): {piso}")
print(f"Teto (para cima): {teto}")
print(f"Inteiro mais próximo: {mais_proximo}")
