#nome = input("Digite o nome do aluno: ")
notas = []

def ler_nota():
    notas.append(float(input("Digite uma nota: ")))

def calcular_media():
 somatorio = sum(notas)
 quantidade_elementos = len(notas)
 media = somatorio / quantidade_elementos
 print("Media:",round(media,2))

ler_nota()
ler_nota()
ler_nota()
ler_nota()
calcular_media()
print("Maior nota:",max(notas))
print("Menor nota:",min(notas))


# print(notas)
# print(len(notas))

# notas.append(7.5)
# notas.append(8.5)
# notas.append(3.5)

# print(notas)

# notas.append(9.3)
# print(notas)
# notas.append(259.90)
# print(notas)

# notas.pop()
# print(notas)

# notas.pop(0)
# print(notas)
# print(len(notas))

# notas[0] = 9.1
# print(notas)
# print(len(notas))
