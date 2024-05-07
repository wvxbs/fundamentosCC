def main():
    valor = int(input("Insira o valor: "))
    bits = quantidadeDeBits(valor)
    converterParaBinario(bits, valor)

def converterParaBinario(bits, valor):
    binario = ""
    _valor = valor
    i = len(bits)
    while len(binario) <= i:
        if _valor >= bits[i]:
            binario += "1"
            _valor -= bits[i]
            print(binario)
            print(_valor)
            i -= 1
        else:
            binario += "0"
            i -= 1

    return binario
            

def quantidadeDeBits(valor):
    arr = [1]
    i = 0
    while arr[i] < valor:
        arr.append(arr[i] * 2)
        i +=1
    print(arr)
    return arr

main()