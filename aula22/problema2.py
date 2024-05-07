def bubbleSort(vetor):
    vetorOrdenado = vetor

    for j in range(len(vetorOrdenado) - 1):
        for i in range(len(vetorOrdenado) - 1):
            if vetorOrdenado[i] > vetorOrdenado[i + 1]:
                vetorOrdenado[i], vetorOrdenado[i + 1] = vetorOrdenado[i + 1], vetorOrdenado[i]
    
    return vetorOrdenado

def exibirVetor(vetor):
    for i in vetor:
        print(str(i).zfill(4))

def main():
    run = True
    livros = []

    while run:
        codigo = input("Insira o código do livro:")
        if codigo == "0":
            run = False
        
        livros.append(int(codigo))

        exibirVetor(bubbleSort(livros))

main()