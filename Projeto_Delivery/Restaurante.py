class Restaurante:

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.cardapio = []

    def adicionar_item_cardapio(self, item_para_aducionar):
        self.cardapio.append(item_para_aducionar)
        
    def getNome(self):
        return self.nome