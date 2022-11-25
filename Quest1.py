import os

try:
   anoNasc= int(input('Insira Seu Ano De Nascimento: '))
   anoAtual = int(input('Insira Seu o Ano Atual: '))
   idade=anoAtual-anoNasc
   meses=idade*12
   dias=idade*365
   semanas=idade*52

   os.system("cls")     #Aqui é para apagar o texto de cima e tem que colocar o import os#
   print(f"\nA pessoa tem {idade} anos\n")
   print(f"\nPodemos concluir que ela tem {meses} meses.\n")
   print(f"\nE exatamente {dias} dias de vida.\n")
   print(f"\nEla possui {semanas} semanas.\n")

except:

   print('Você Informou Uma Informação Invalida!')

input("\nDigite Qualque Tecla Para Continuar")