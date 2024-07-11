class Pessoa:
  def __init__(self, nome="", sexo="", cpf="", ano_nascimento = 0, salário_bruto= 0.0):          
      self.nome = nome
      self.sexo = sexo
      self.cpf = cpf
      self.ano_nascimento = ano_nascimento
      self.idade = self.calcular_idade()
      self.salário_bruto = salário_bruto
      self.salário_líquido = self.calcular_salário_líquido()
      
  def imprimir_dados_pessoais(self):
    print(f"|>>>| DADOS PESSOAIS |<<<|\n")
    print(f"Nome:{self.nome}")
    print(f"Sexo:{self.sexo}")
    print(f"CPF:{self.cpf}")
    print(f"Idade:{pessoa_1.idade}")
    

  def calcular_idade(self):
    return 2024 - self.ano_nascimento
  
  def calcular_desconto_inss(self):
    salário = self.salário_bruto
    if salário <= 1412.00:
      return self.calcular_porcentagem(7.5)
    elif salário > 1412.00 and salário <= 2666.68:
        return self.calcular_porcentagem(9.00)
    elif salário > 2666.68 and salário <= 4000.03:
        return self.calcular_porcentagem(12.00)
    else:
       return self.calcular_porcentagem(14.00)
    
  def calcular_desconto_irrf(self):
    salário = self.salário_bruto
    if salário >= 2259.21 and salário <= 2826.65:
      return self.calcular_porcentagem(7.5)
    elif salário >= 2826.65 and salário <= 3751.05:
        return self.calcular_porcentagem(15.00)
    elif salário > 3751.06 and salário <= 4664.68:
        return self.calcular_porcentagem(22.5)
    elif salário > 4664.68:
       return self.calcular_porcentagem(27.5)
    else:
       return 
     
    
  def calcular_porcentagem(self, porcentagem):
      return (self.salário_bruto * porcentagem) / 100
  
  def imprimir_dados(self):
      print(f"Nome:{self.nome} \n {self.ano_nascimento} \n{self.cpf} \n{self.sexo} \n{self.salário_bruto} {self.salário_líquido}\n {self.idade}")

  def calcular_salário_líquido(self):
     return self.salário_bruto - (self.calcular_desconto_inss() + self.calcular_calcular_desconto_irrf())
    
if __name__ == '__main__':
  pessoa_1 = Pessoa("André", "Masculino", "111.222.333-44", 2005, 2826.65)
  pessoa_1.imprimir_dados_pessoais()
  #print(round(pessoa_1.salário_líquido,2))
  pessoa_2 = Pessoa()
  pessoa_2.nome = input("Digite o seu nome:")
  pessoa_2.cpf = input("Digite o seu cpf:")
  pessoa_2.salário_bruto = float(input("Digite o seu salário bruto:"))
  pessoa_2.ano_nascimento = int (input("Digite o seu ano de nascimento:"))
  pessoa_2.sexo = input("Digite o seu sexo:")
  pessoa_2.salário_líquido = pessoa_2.calcular_salário_líquido()
  pessoa_2.idade = pessoa_2.calcular_idade()
  pessoa_2.imprimir_dados


  


  
  
      
  #pessoa_input = Pessoa()

  #def calcular_salário(self):
  #  input("Digite o valor do seu salário bruto:")

  #pessoa_input.salário = input("Digite seu salário bruto:")
  #print(pessoa_input.salário_bruto) / 100