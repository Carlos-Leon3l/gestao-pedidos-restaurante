class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
    def getNome(self):
        return self.nome  
    
    def getEndereco(self):
        return self.endereco