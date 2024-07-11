nome = str(input("Digite seu nome:"))
valor = float(input(f"Digite o valor inicial que conterá em sua conta:"))
saldo = float
opção = int
Extrato = str, float
Sacar = float
saques = float
Depositar = float
depósitos = float
saldo = float
sair = str

opçao = ""

def imprimir_menu():
    print("----------------------------")
    print(">>> | MENU DE OPÇÕES | <<<")
    print("----------------------------")
    print("[1] Extrato")
    print("[2] Sacar")
    print("[3] Depositar")
    print("[4] Sair")
    print("----------------------------")

while opçao != 4:
    imprimir_menu()
    opçao = int(input("Escolha uma opção: "))
    if opçao == 1:
        print(f"{saldo}")
        print(f"Saques:{saques}") 
        print(f"Depósitos:{depósitos}")

    elif opçao == 2:
        input("Digite o valor que deseja sacar:")
        print(f"{saldo}")
    elif opçao == 3:
        input("Digite o valor que deseja depositar:")
        print(f"{saldo}")
    else:
        print("Saindo...")

def extrato():
 (print(f"{nome}, seu saques foram:{saques}, sua quantidade de depósitos realizados foram:{depósitos}, seu saldo em conta:{saldo}.")) 
def sacar():
 (print(f"Qual valor deseja sacar?(OBS: O valor não pode ser superior ao saldo) Digite um valor:"))
def depositar():
 (print(f"Digite o valor que deseja depositar:, saldo atualizado {saldo}")) 
def sair():
 (print(f"Saindo...{sair}"))

 