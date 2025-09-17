class Lanche:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes

    def exibirLanches(self):
        """
        Exibe os dados do lanche cadastrado (nome, preco e ingredientes[])
        """
        print(f"Sanduíche: {self.nome}; Preço: {self.preco}; Ingredientes: {self.ingredientes}")