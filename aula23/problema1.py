def bubbleSort(vetor):
    vetorOrdenado = vetor

    for j in range(len(vetorOrdenado) - 1):
        for i in range(len(vetorOrdenado) - 1):
            if vetorOrdenado[i] > vetorOrdenado[i + 1]:
                vetorOrdenado[i], vetorOrdenado[i + 1] = vetorOrdenado[i + 1], vetorOrdenado[i]
    
    return vetorOrdenado

def exibirVetor(vetor):
    for i in vetor:
        print(i)

def exibirVencedor(vetor, escolhido):
    print(f"Aluno escolhido: {vetor[escolhido]}")

def main():
    nomes = []
    
    quantidade, escolhido = input("Insira a quantidade de alunos e o vencedor: ").split(" ")

    for i in range(int(quantidade)):
        nome = input("Insira o nome: ")
        nomes.append(nome)

    nomesOrdenados = bubbleSort(nomes)

    exibirVetor(nomesOrdenados)
    exibirVencedor(nomesOrdenados, int(escolhido))

main()