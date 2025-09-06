
class Entrega:
    def __init__(self, metodo_entrega):
        self.metodo_entrega = metodo_entrega
        self.taxa_entrega = 0

        if(self.metodo_entrega == "COMUM".upper()):
            print("Escolhido: Entrega normal. Sem custos adicionais")
            #print("sem custos adicionais")
            self.taxa_entrega = 0

        elif(self.metodo_entrega == "RAPIDO".upper()):
            print(" Escolhido: Entrega Rápida. Custo adicional de 5 reais")
            self.taxa_entrega = 5
            
    def getTaxa(self):
        return self.taxa_entrega 
