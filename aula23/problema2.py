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

def extrairDados(dado, vetor):
    acc = 0

    for i in vetor:
        if i[0] == dado:
            acc +=1

    return acc

def validarNome(nome):
    if nome[0] == "-" or nome[0] == "+":
        return True

    return False

def main():
    run = True
    nomes = []

    while run:
        nome = input("Insira o nome: ")

        if validarNome(nome):
            nomes.append(nome)
        else:
            print("Nome inváldo")

        nomesOrdenados = bubbleSort(nomes)
        qtdMais = extrairDados("+", nomesOrdenados)
        qtdMenos = extrairDados("-", nomesOrdenados)

        exibirVetor(nomes)
        print(f"Se comportaram: {qtdMais}")
        print(f"Não se comportaram: {qtdMenos}")

main()