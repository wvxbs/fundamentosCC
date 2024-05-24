def bubbleSort(vetor, exp):
    n = len(vetor)
    vetorOrdenado = vetor
    
    for j in range(n - 1):
        for i in range(n - 1):
            if (vetorOrdenado[i] // exp) % 10 > (vetorOrdenado[i + 1] // exp) % 10:
                vetorOrdenado[i], vetorOrdenado[i + 1] = vetorOrdenado[i + 1], vetorOrdenado[i]
    
    return vetorOrdenado

def radixSort(vetor):
    valorMaximo = max(vetor)
    exp = 1

    while valorMaximo // exp > 0:
        vetorOrdenado = bubbleSort(vetor, exp)
        exp *= 10

    return vetorOrdenado

def main():
    vetor = [10, 154, 8, 0, 9, 48, 7, 55, 5]

    print(f"Vetor desordenado: {vetor}") 

    vetorOrdenado = radixSort(vetor)
    print(f"Vetor ordenado: {vetorOrdenado}")

main()