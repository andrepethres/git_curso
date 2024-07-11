idade = int(input("Digite sua idade por gentileza:"))

if idade >= 18 and idade <= 70:
 print("Voto obrigatório")
elif idade >= 16 or idade < 70:
 print("Voto facultativo")
else:
 print("Voto proibido")
		