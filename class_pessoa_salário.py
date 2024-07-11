class Pessoa:
  def __init__(self, nome="", sexo="", cpf="", ano_nascimento=0, salário_líquido="", salário_bruto="", valor=""):          
      self.nome = nome
      self.sexo = sexo
      self.cpf = cpf
      self.ano_nascimento = ano_nascimento
      self.idade = self.calcular_idade()
      self.salário_bruto = salário_bruto
      self.salário_líquido = salário_líquido
      self.salário_líquido = self.calcular_salário()
      self.valor = valor

  def imprimir_dados_pessoais(self):
    print(f"|>>>| DADOS PESSOAIS |<<<|\n")
    print(f"Nome:{self.nome}")
    print(f"Sexo:{self.sexo}")
    print(f"CPF:{self.cpf}")
    print(f"Idade:{pessoa_1.idade}")
    
  #calcular_idade
  def calcular_idade(self):
    return 2024 - self.ano_nascimento
  #calcular_salário
  #def calcular_salário(self):
    #if self.salário_bruto == 2826,65
  #porcentagem
  def porcentagem(self):
      self.valor = float(input("Digite um valor de porcentagem:"))
      if 1000 * 10 / 100 = 100

      elif
  
if __name__ == '__main__':
  pessoa_1 = Pessoa ("André", "Masculino", "111.222.333-44", 2005, 2826,65, 101,18, 169,44, 50%)

  pessoa_1.imprimir_dados_pessoais()
      
  #pessoa_input = Pessoa()

  #def calcular_salário(self):
    #input("Digite o valor do seu salário bruto:")

  #pessoa_input.salário = input("Digite seu salário bruto:")
  #print(pessoa_input.salário_bruto)
  



  
 



