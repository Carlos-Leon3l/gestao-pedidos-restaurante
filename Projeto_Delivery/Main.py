
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
        

class ItemCardapio:
    def __init__(self, nome_item:str, descricao:str, preco:int):
        self.nome_item = nome_item
        self.descricao = descricao
        self.preco = preco
    
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
        pass
        
    def calcular_valor_total_pedido(self):
        soma_itens = 0
        print("DEBUG: Conteúdo da lista de itens:", self.lista_itens)
        for item in self.lista_itens:
            preco = item.getPreco()
            soma = preco
            soma_itens = soma_itens + soma
        self.valor_total = soma_itens
        return self.valor_total
   
        # if(self.info_pagamento.escolher_forma_pagamento()):
        #     for item in self.lista_itens:
        #         preco_item = item.getPreco()
        #         valor_total_itens =+ preco_item
        #     valor_total_itens + self.detalhes_entrega.getTaxa()
        # self.valor_total = valor_total_itens
        # return self.valor_total
 
    def status_do_pedido_atual(self):
        self.status_entrega = "A CAMINHO"
        
    def definir_entrega(self, objeto_entrega):
        self.definir_entrega = objeto_entrega
        pass
        
class Pagamento:
    def __init__(self, metodo_pagamento):
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
            
        elif(self.metodo_pagamento == "PIX".upper()):
            print("Seu pagamento foi efetuado, compra a caminho")
        
        elif(self.metodo_pagamento == "Dinheiro".upper()):
            print("Pague na hora do pedido ser entregue a sua casa")
             
            
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

    
h = Pedido(Cliente("c","madre",24124),Restaurante("pizza","italiana"))

h.adicionar_item(ItemCardapio("pizza","pizzalegal",20))
h.adicionar_item(ItemCardapio("pizza","pizzalegal",50))


print(h.calcular_valor_total_pedido())
 