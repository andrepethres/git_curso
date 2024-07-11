# Escreva um programa por meio de pseudocódigo para solicitar ao usuário quatro notas de um aluno, e o seu nome; calcular a média e mostrar o nome do aluno e sua média.

nome_aluno = str(input("Digite seu nome:"))
primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input("Digite a segunda nota:"))
terceira_nota = float(input("Digite a terceira nota:"))
quarta_nota = float(input("Digite a quarta nota:"))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota)/4
print (nome_aluno, "Está com média:", media)



