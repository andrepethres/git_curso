print(">>>|CRIPTOGRAFE E DESCRIPTOGRAFE SUA FRASE|<<<\n")
def cripto(frase):
 tradutor = ""
 for letra in frase:
     
    if letra in "Aa": tradutor = tradutor + "r"
    elif letra in "Bb": tradutor = tradutor + "f"
    elif letra in "Cc": tradutor = tradutor + "y"
    elif letra in "Dd": tradutor = tradutor + "p"
    elif letra in "Ee": tradutor = tradutor + "x"
    elif letra in "Ff": tradutor = tradutor + "z"
    elif letra in "Gg": tradutor = tradutor + "w"
    elif letra in "Hh": tradutor = tradutor + "t"
    elif letra in "Ii": tradutor = tradutor + "i"
    elif letra in "Jj": tradutor = tradutor + "v"
    elif letra in "Kk": tradutor = tradutor + "a"
    elif letra in "Ll": tradutor = tradutor + "h"
    elif letra in "Mm": tradutor = tradutor + "u"
    elif letra in "Nn": tradutor = tradutor + "j"
    elif letra in "Oo": tradutor = tradutor + "s"
    elif letra in "Pp": tradutor = tradutor + "q"
    elif letra in "Qq": tradutor = tradutor + "c"
    elif letra in "Rr": tradutor = tradutor + "b"
    elif letra in "Ss": tradutor = tradutor + "m"
    elif letra in "Tt": tradutor = tradutor + "n"
    elif letra in "Uu": tradutor = tradutor + "ç"
    elif letra in "Vv": tradutor = tradutor + "d"
    elif letra in "Ww": tradutor = tradutor + "o"
    elif letra in "Xx": tradutor = tradutor + "g"
    elif letra in "Yy": tradutor = tradutor + "a"
    elif letra in "Zz": tradutor = tradutor + "e"
    elif letra in "Kk": tradutor = tradutor + "ç"

 print(tradutor)
(cripto(input("Por gentileza, digite a frase que deseja criptografar:")))
input("Frase criptografada com sucesso!")

def descripto(frase):
  tradutor = ""
  for letra in frase:

    if letra in "Rr": tradutor = tradutor + "a"
    elif letra in "Ff": tradutor = tradutor + "b"
    elif letra in "Yy": tradutor = tradutor + "c"
    elif letra in "Pp": tradutor = tradutor + "d"
    elif letra in "Xx": tradutor = tradutor + "e"
    elif letra in "Zz": tradutor = tradutor + "f"
    elif letra in "Ww": tradutor = tradutor + "g"
    elif letra in "Tt": tradutor = tradutor + "h"
    elif letra in "Ii": tradutor = tradutor + "i"
    elif letra in "Vv": tradutor = tradutor + "j"
    elif letra in "Aa": tradutor = tradutor + "k"
    elif letra in "Hh": tradutor = tradutor + "l"
    elif letra in "Uu": tradutor = tradutor + "m"
    elif letra in "Jj": tradutor = tradutor + "n"
    elif letra in "Ss": tradutor = tradutor + "o"
    elif letra in "Qq": tradutor = tradutor + "p"
    elif letra in "Qq": tradutor = tradutor + "q"
    elif letra in "Bb": tradutor = tradutor + "r"
    elif letra in "Mm": tradutor = tradutor + "s"
    elif letra in "Nn": tradutor = tradutor + "t"
    elif letra in "Çç": tradutor = tradutor + "u"
    elif letra in "Dd": tradutor = tradutor + "v"
    elif letra in "Oo": tradutor = tradutor + "w"
    elif letra in "Gg": tradutor = tradutor + "x"
    elif letra in "Aa": tradutor = tradutor + "y"
    elif letra in "Ee": tradutor = tradutor + "z"
    elif letra in "Çç": tradutor = tradutor + "k"
    else:
      tradutor = tradutor + letra

  print(tradutor)
(descripto(input("Digite a frase criptografada caso deseja descriptografar:")))
input("Frase descriptografada com sucesso!\n")
input("VOLTE SEMPRE GUERREIRO(A)!")



    
















