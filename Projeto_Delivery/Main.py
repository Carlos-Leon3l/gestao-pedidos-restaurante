from Pedido import Pedido
from Cliente import Cliente
from Restaurante import Restaurante
from ItemCardapio import ItemCardapio
from Entrega import Entrega
from Pagamento import Pagamento


    
pedido_cliente = Pedido(Cliente("carlos","madre",24124),Restaurante("pizzaria","italiana"))

pedido_cliente.adicionar_item(ItemCardapio("pizza peperroni","boa pizza",20))

pedido_cliente.adicionar_item(ItemCardapio("pizza de mussarela","essa e tbm uma boa pizza",50))

entrega = Entrega("RAPIDO")

pagamento = Pagamento("PIX")

print(pagamento.escolher_forma_pagamento())

pedido_cliente.valor_taxa_produto(entrega.getTaxa())

pedido_cliente.calcular_valor_total_pedido()

print(pedido_cliente.recibo_de_entrega())