def decParaBase(decimal, base):
    valorConvertido = ""

    while decimal !=0:
        match decimal % base:
            case 10: valorConvertido += "A"
            case 11: valorConvertido += "B"
            case 12: valorConvertido += "C"
            case 13: valorConvertido += "D"
            case 14: valorConvertido += "E"
            case 15: valorConvertido += "F"
            case _: valorConvertido += str(decimal % base)
        
        decimal //= base

    return valorConvertido

def basePraDec(numero, base):
    numero = numero.upper()
    decimal, expoente = 0,0

    for i in range(len(numero)):
        match numero[i]:
            case "A": digito = 10
            case "B": digito = 11
            case "C": digito = 12
            case "D": digito = 13
            case "E": digito = 14
            case "F": digito = 15
            case _: 
                digito = int(numero[i])
                decimal += int(digito) * base ** (-(expoente - (len(numero)- 1)))
                expoente += 1

    return decimal

def main():
    numero, base, operacao = input().split(" ")

    match int(operacao):
        case 0:
            print(decParaBase(int(numero), int(base)))
        case 1:
            print(basePraDec(numero, int(base)))
        case _:
            print("Insira uma operação válida!")

main()