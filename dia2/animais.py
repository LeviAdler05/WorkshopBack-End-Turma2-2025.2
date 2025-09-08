# dia2/animais.py
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som genérico de animal"

    def apresentar(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos. 🐾"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        return [f"{a.apresentar()} Faz: {a.falar()}" for a in self.animais]

    def filtrar_por_tipo(self, tipo):
        return [a for a in self.animais if isinstance(a, tipo)]

# Exemplo de uso:
if __name__ == "__main__":
    zoo = Zoologico()
    gato1 = Gato("Felix", 3)
    cachorro1 = Cachorro("Rex", 5)
    gato2 = Gato("Mimi", 2)
    zoo.adicionar_animal(gato1)
    zoo.adicionar_animal(cachorro1)
    zoo.adicionar_animal(gato2)

    print("Todos os animais:")
    for info in zoo.listar_animais():
        print(info)

    print("\nApenas gatos:")
    for gato in zoo.filtrar_por_tipo(Gato):
        print(gato.apresentar(), "Faz:", gato.falar())
