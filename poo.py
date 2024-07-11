class cachorro:
   def __init__(self, raça, cor, nome, sexo, peso, altura, data_nascimento, quantidade_comida_porção):
      self.peso = peso
      self.cor = cor
      self.nome = nome
      self.raça = raça
      self.altura = altura
      self.data_nascimento = data_nascimento
      self.sexo = sexo
      self.quantidade_comida_porção = quantidade_comida_porção
      self.comida = 1000
   
   def imprimir_relatório(self):
      print(f"----DADOS DO PET----\n")
      print(f"Raça:{self.raça}")
      print(f"Cor:{self.cor}")
      print(f"Nome:{self.nome}")
      print(f"Sexo:{self.sexo}")
      print(f"Peso:{self.peso}")
      print(f"Altura:{self.altura}")
      print(f"Data de nascimento:{self.data_nascimento}") 

   def comer(self):
      self.comida -= self.quantidade_comida_porção
      print(f"Quanto sobrou de ração no fim do mês:{self.nome} ainda possui {self.comida} gramas de ração neste final do mês.")     
      
if __name__ == '__main__':
   meu_primeiro_cachorro = cachorro("Pintscher", "Preto e amarelo", "Pingo", "Macho", 5.590, 32.5, "01/01/2024",700)

   meu_primeiro_cachorro.imprimir_relatório()
   meu_primeiro_cachorro.comer()
   
   
   


   
