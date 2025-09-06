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