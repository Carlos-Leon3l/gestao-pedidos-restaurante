from Cliente import Cliente
from Restaurante import Restaurante
from ItemCardapio import ItemCardapio

#Conector
class Pedido:
    def __init__(self, nome_cliente_pedido:Cliente, 
                restaurante:Restaurante):
        self.nome_cliente_pedido = nome_cliente_pedido.getNome()
        self.restaurante = restaurante
        self.lista_itens = []
        self.status_entrega = "PEDENTE"
        self.valor_total = 0
        self.detalhes_entrega = None
        self.info_pagamento = None
    
    def adicionar_item(self, item_novo:ItemCardapio):
        self.lista_itens.append(item_novo)
    
    def definir_pagamento(self, objeto_pagamento):
        self.info_pagamento = objeto_pagamento
        return self.info_pagamento
        
    def calcular_valor_total_pedido(self):
        soma_itens = 0
    
        for item in self.lista_itens:
            preco = item.getPreco()
            soma = preco
            soma_itens = soma_itens + soma
        self.valor_total = soma_itens
        self.detalhes_entrega = self.valor_total + self.detalhes_entrega
        return f"Valor total do Pedido: {self.detalhes_entrega}"
   
    def status_do_pedido_atual(self):
        self.status_entrega = "A CAMINHO"
        
    def valor_taxa_produto(self, opcao_de_entrega_escolhida):
        self.detalhes_entrega = opcao_de_entrega_escolhida
        
    def recibo_de_entrega(self):
        print("Recibo do Pedido:")
        print(f"NOME DO CLIENTE: {self.nome_cliente_pedido}")
        print(f"NOME DO PEDIDO: {self.restaurante.getNome()}")
        print(f"LISTA DE PEDIDO:")
        for itens in self.lista_itens:
             print(f"[{itens.getNome()}, {itens.getDescricao()},{itens.getPreco()}]")
        print(f"VALOR TOTAL DO PEDIDO: {self.detalhes_entrega}")