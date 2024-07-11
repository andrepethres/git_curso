# Escreva um programa por meio de pseudocódigo para solicitar ao usuário quatro notas de um aluno, e o seu nome; calcular a média e mostrar o nome do aluno e sua média.

nome = str(input("Digite seu nome: \n"))
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))
quarta_nota = float(input("Digite a quarta nota: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
# print("O Aluno:", nome , "ficou com média:", media)
print(f"O aluno: {nome} ficou com média: {media}")

print (f"As notas do aluno foram: {primeira_nota , segunda_nota, terceira_nota, quarta_nota} e a média ficou: {media}")

# Print("As notas do aluno foram: (",primeira_nota,",",segunda_nota,",",terceira_nota,",",quarta_nota,") e a média ficou:",media)

if media >= 7.0:
    print(f"O Aluno {nome} está aprovado!")

elif media >= 5: 
    print(f"O Aluno {nome} está em recuperação.")

else:
    print(f"O Aluno {nome} está reprovado.")


    






