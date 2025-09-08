'''
# 1 SyntaxError: '(' was never closed
print("Ola Mundo!")

# 2 NameError: name 'nome' is not defined. Did you mean: 'None'?
nome = "Levi"
print(nome)

# 3 TypeError: unsupported operand type(s) for +: 'int' and 'str'
def soma(a, b):
    return a + b

resultado = soma(10, 5)
print(resultado)


# 4 ValueError: invalid literal for int() with base 10:
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: "))
try:
    print(numeros[indice])
except IndexError:
        print("indice inválido")
    
print(numeros[indice])



# 5 ValueError: invalid literal for int() with base 10: 'a'
def dividir(a, b):
    return a / b

try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: não pode dividir por zero.")


# 6 KeyError:
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

try:
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    valor = dados.get(chave, f"Chave '{chave}' não encontrada.")
    print(f"Erro: a chave '{chave}' não existe no dicionário.")



# 7 IndentationError: unexpected indent
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")
    return f"Idade válida: {idade}"

while True:
    try:
        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        break
    except ValueError as e:
        print(f"Erro: {e} Tente novamente.")
'''

# 8 TypeError: unsupported operand type(s) for +: 'int' and 'str'
def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

entrada = input("Digite as notas separadas por espaço: ")

try:
    notas = list(map(float, entrada.split()))
    media = calcular_media(notas)
    print(f"Média: {media:.2f}")
except ValueError:
    print("Erro: digite apenas números válidos.")
