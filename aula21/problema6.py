def imprimirImagem(imagem):
    simbolos = [" ", "*"]
    ehBranco = True

    for i in imagem:
        for j in i:
            for x in range(j):
                print(simbolos[0 if ehBranco else 1], end=" ")
        
            ehBranco = not ehBranco
                    
        print("")

def main():
    imagem = [
        [6, 2, 6],
        [6, 2, 6],
        [6, 2, 6],
        [4, 6, 4],
        [2, 10, 2],
        [0, 14],
        [0, 14],
        [0, 4, 2, 2, 2, 4],
        [0, 2, 4, 2, 4, 2],
        [6, 2, 6],
        [4, 6, 4],
        [2, 10, 2],
        [2, 2, 2, 2, 2, 2, 2]
    ]

    imprimirImagem(imagem)

main()