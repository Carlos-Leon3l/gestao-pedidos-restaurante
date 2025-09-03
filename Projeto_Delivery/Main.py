
from time import sleep

class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
    def getNome(self):
        return self.nome  
    
    def getEndereco(self):
        return self.endereco

class Restaurante:

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.cardapio = []

    def adicionar_item_cardapio(self, item_para_aducionar):
        self.cardapio.append(item_para_aducionar)
        
    def getNome(self):
        return self.nome
        
class ItemCardapio:
    def __init__(self, nome_item:str, descricao:str, preco:int):
        self.nome_item = nome_item
        self.descricao = descricao
        self.preco = preco
        
    def getNome(self):
        return self.nome_item 
    
    def getDescricao(self):
        return self.descricao
    
    def getPreco(self):
        return self.preco
        

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
        print("DEBUG: Conteúdo da lista de itens:", self.lista_itens)
        for item in self.lista_itens:
            preco = item.getPreco()
            soma = preco
            soma_itens = soma_itens + soma
        self.valor_total = soma_itens
        self.detalhes_entrega = self.valor_total + self.detalhes_entrega
        return self.detalhes_entrega
   
    def status_do_pedido_atual(self):
        self.status_entrega = "A CAMINHO"
        
    def valor_taxa_produto(self, opcao_de_entrega_escolhida):
        self.detalhes_entrega = opcao_de_entrega_escolhida
        
    def recibo_de_entrega(self):
        print(f"NOME DO CLIENTE: {self.nome_cliente_pedido}")
        print(f"NOME DO PEDIDO: {self.restaurante.getNome()}")
        print(f"LISTA DE PEDIDO:")
        for itens in self.lista_itens:
             print(f"[{itens.getNome()}, {itens.getDescricao()},{itens.getPreco()}] \n")
        print(f"VALOR TOTAL DO PEDIDO: {self.detalhes_entrega}")
    
class Pagamento:
    def __init__(self, metodo_pagamento:str):
        self.metodo_pagamento = metodo_pagamento
        self.status_pagamento = "PENDENTE"
    
    def escolher_forma_pagamento(self):
        self.processamento_do_pagamento()
        self.status_pagamento = "APROVADO"
        return self.status_pagamento
            
    def processamento_do_pagamento(self):
        if(self.metodo_pagamento == "Cartao".upper()):
            print("Pagamento esta sendo processado ....")
            sleep(5)
            print("Seu pagamento foi efetuado, compra a caminho")
            return self.metodo_pagamento
            
        elif(self.metodo_pagamento == "PIX".upper()):
            print("Seu pagamento foi efetuado, compra a caminho")
            return self.metodo_pagamento

        elif(self.metodo_pagamento == "Dinheiro".upper()):
            print("Pague na hora do pedido ser entregue a sua casa")
            return self.metodo_pagamento

            
class Entrega:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega
        self.taxa_entrega = 0

        if(self.metodo_entrega == "COMUM".upper()):
            #print("metodo de entrega comum")
            #print("sem custos adicionais")
            self.taxa_entrega = 0

        elif(self.metodo_entrega == "RAPIDO".upper()):
            #print("Custo adicional de 5 reais")
            self.taxa_entrega = 5
            
    def getTaxa(self):
        return self.taxa_entrega 

    
pedido_cliente = Pedido(Cliente("carlos","madre",24124),Restaurante("pizzaria","italiana"))

pedido_cliente.adicionar_item(ItemCardapio("pizza peperroni","boa pizza",20))

pedido_cliente.adicionar_item(ItemCardapio("pizza de mussarela","essa e tbm uma boa pizza",50))

entrega = Entrega("RAPIDO")

pagamento = Pagamento("PIX")

print(pagamento.escolher_forma_pagamento())

pedido_cliente.valor_taxa_produto(entrega.getTaxa())

print(pedido_cliente.calcular_valor_total_pedido())

print(pedido_cliente.recibo_de_entrega())
 