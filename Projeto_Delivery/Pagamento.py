from time import sleep

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
