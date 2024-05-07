import random

def gerarVetor(seed):
    vetor = []

    while len(vetor) < seed:
        vetor.append(random.randint(0, seed))

    return vetor

def bubbleSort(vetor):
    vetorOrdenado = vetor

    for j in range(len(vetorOrdenado) - 1):
        for i in range(len(vetorOrdenado) - 1):
            if vetorOrdenado[i] > vetorOrdenado[i + 1]:
                vetorOrdenado[i], vetorOrdenado[i + 1] = vetorOrdenado[i + 1], vetorOrdenado[i]
    
    return vetorOrdenado

def main():
    tamanho = int(input("Insira a quantidade de valores da lista: "))
    vetor = gerarVetor(tamanho)
    print(f"Vetor sem ordenação: {vetor}")
    print(f"Vetor ordenado: {bubbleSort(vetor)}")

main()
