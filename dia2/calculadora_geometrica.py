#  Calculadora geométrica avançada com funções para área de círculo, área de triângulo e hipotenusa

import math

class FiguraGeometrica:
    def area_circulo(self, raio):
        return math.pi * math.pow(raio, 2)

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def hipotenusa(self, cateto1, cateto2):
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

if __name__ == "__main__":
    figura = FiguraGeometrica()
    print("Escolha o cálculo:")
    print("1 - Área do círculo")
    print("2 - Área do triângulo")
    print("3 - Hipotenusa do triângulo retângulo")
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        raio = float(input("Digite o raio do círculo: "))
        area = figura.area_circulo(raio)
        print(f"Área do círculo: {area}")
    elif escolha == "2":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = figura.area_triangulo(base, altura)
        print(f"Área do triângulo: {area}")
    elif escolha == "3":
        cateto1 = float(input("Digite o valor do primeiro cateto: "))
        cateto2 = float(input("Digite o valor do segundo cateto: "))
        hipo = figura.hipotenusa(cateto1, cateto2)
        print(f"Hipotenusa: {hipo}")
    else:
        print("Opção inválida.")
