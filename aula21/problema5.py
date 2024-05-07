def imprimirImagem(imagem):
    simbolos = [" ", "*"]

    for i in imagem:
        for j in i:
            print(simbolos[0 if j == 0 else 1], end=" ")
                  
        print("")

def main():
    imagem = [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    ]

    imprimirImagem(imagem)

main()