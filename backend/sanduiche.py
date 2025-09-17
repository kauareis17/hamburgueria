class Lanche:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

ingredientes = []
nome = input("Nome do sanduíche: ")
preco = float(input("Preço do sanduíche: "))

for item in range(6):
    ingredientes = input(f"Informe o ingredientes: {item-1} ")
    ingredientes.append

l = Lanche

print(f"Sanduíche:{l.nome}; Preço: {l.preco}; Ingredientes: {l.ingredientes}")

