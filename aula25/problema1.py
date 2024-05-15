import turtle

def percorrerMatriz(tartaruga, matriz, cores, tamanhoDoPixel):
    for i in matriz:
        for j in i:
            tartaruga.fillcolor(f"#{cores[j]}")
            tartaruga.begin_fill()

            for lado in range(4):
                tartaruga.forward(tamanhoDoPixel)
                tartaruga.right(90)
            
            tartaruga.end_fill()
            tartaruga.forward(tamanhoDoPixel)

        tartaruga.backward(tamanhoDoPixel * len(i))
        tartaruga.right(90)
        tartaruga.forward(tamanhoDoPixel)
        tartaruga.left(90)

    tartaruga.done()

def configurarDesenho(tartaruga, coordenadaX, coordenadaY):
    tartaruga.penup()
    tartaruga.speed(0)
    tartaruga.goto(float(coordenadaX), float(coordenadaY))

    return tartaruga

def teste1():
    cores = ["FFF", "000", "F80500", "F7C192"]
    matriz = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],[0,0,0,1,1,0,0,2,2,0,0,1,1,0,0,0],[0,0,1,0,0,0,2,2,2,2,0,0,0,1,0,0],[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],[1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,1],[0,1,1,1,3,3,1,3,3,1,3,3,1,1,1,0],[0,0,1,3,3,3,1,3,3,1,3,3,3,1,0,0],[0,0,1,3,3,3,3,3,3,3,3,3,3,1,0,0],[0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]]

    return cores, matriz

def teste2():
    cores = ["FFF", "000", "F80500", "F7C192", "FDFD11", "0071C1", "9D4700"]
    matriz = [[0,0,0,2,2,2,2,2,2,0,0,0,0],[0,0,2,2,2,2,2,2,2,2,2,2,2,0],[0,0,6,6,6,3,3,3,1,3,0,0,0,0],[0,6,3,6,3,3,3,3,1,3,3,3,3,0],[0,6,3,6,6,3,3,3,3,1,3,3,3,3],[0,6,6,3,3,3,3,3,1,1,1,1,0,0],[0,0,0,3,3,3,3,3,3,3,3,0,0,0],[0,0,2,2,5,2,2,2,2,0,0,0,0,0],[0,2,2,2,5,2,2,5,2,2,2,0,0,0],[2,2,2,2,5,5,5,5,2,2,2,2,2,0],[3,3,2,5,4,5,5,4,5,2,3,3,3,0],[3,3,3,5,5,5,5,5,5,5,3,3,3,0],[3,3,5,5,5,5,5,5,5,5,3,3,3,0],[0,0,5,5,5,0,0,5,5,5,0,0,0,0],[0,6,6,6,0,0,0,0,6,6,6,0,0,0],[6,6,6,6,0,0,0,0,6,6,6,6,0,0]]

    return cores, matriz

def main():
    coordenadaX, coordenadaY = input("Insira a posição X, e Y(separadas por espaço) para iniciar o desenho: ").split(" ")
    tamanhoDoPixel = float(input("Insira o tamanho do píxel: "))
    cores, matriz = None, None

    escolha = input("Insira o teste desejado (1 ou 2): ")

    while(True):
        match escolha:
            case "1":
                cores, matriz = teste1()
            case "2":
                cores, matriz = teste2()
            case _:
                print("Insira um caso de teste válido!")

        tartaruga = configurarDesenho(turtle.Turtle(), coordenadaX, coordenadaY)
        percorrerMatriz(tartaruga, matriz, cores, tamanhoDoPixel)


main()