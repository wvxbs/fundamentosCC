def ConverterBaseNParaDecimal(numero, base):
  decimal, expoente = 0,0

  for indice in range(len(numero)):
    if numero[indice] == 'A': 
      digito = 10

    elif numero[indice] == 'B':
      digito = 11

    elif numero[indice] == 'C':
        digito = 12

    elif numero[indice] == 'D':
        digito = 13

    elif numero[indice] == 'E':
        digito = 14

    elif numero[indice] == 'F':
        digito = 15

    else:
        digito = int(numero[indice])
        decimal += int(digito) * base ** (-(expoente - (len(numero) - 1)))
        expoente += 1
      
    return decimal

def converterDecimalParaBaseN(decimal, base):
  valorConvertido = ""
  
  while decimal != 0:
    if decimal % base <= 9:
      valorConvertido += str((int(decimal % base)))
      decimal //= base

    elif decimal % base == 10:
      valorConvertido += ("A")
      decimal //= base

    elif decimal % base == 11:
      valorConvertido += ("B")
      decimal //= base

    elif decimal % base == 12:
      valorConvertido += ("C")
      decimal //= base

    elif decimal % base == 13:
      valorConvertido += ("D")
      decimal //= base

    elif decimal % base == 14:
      valorConvertido += ("E")
      decimal //= base

    elif decimal % base == 15:
      valorConvertido += ("F")
      decimal //= base

  return valorConvertido[::-1]

def main():
  run = True

  while(run):
    print("[1] - Converter de binário/octal/hexadecimal para decimal: \n[2] - Converter de decimal para binário/octal/hexadecimal: \n[3] - Informações do grupo: \n[4] - Sair: ")
    escolha = int(input("Digite uma opção: "))

    match escolha:
      case 1:
        numero = input('Digite o número a ser convertido: ')
        base = int(input('Informe a base do número digitado (2, 8 ou 16): '))
        print(f"{numero} === {ConverterBaseNParaDecimal(numero, base)}\n")

      case 2:
        numero = int(input('Digite um número decimal inteiro: '))
        base = int(input('Escolha a base para converter (2, 8 ou 16): '))
        print(f"{numero} === {converterDecimalParaBaseN(numero, base)}\n")

      case 3:
        print("Gabriel Ferreira:\n Tia: 32475810 Ra: 10442043\n")
        print("Gabriel Mires Camargo:\n Tia: 32427719 Ra: 10436741\n")
        
      case 4:
        run = False

main()