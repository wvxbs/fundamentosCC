import turtle

# Criando a tela e o objeto Turtle
tela = turtle.Screen()
tartaruga = turtle.Turtle()

# Desenhando o quadrado
for _ in range(4):
    tartaruga.forward(100)  # Avança 100 unidades
    tartaruga.right(90)     # Vira 90 graus para a direita

# Finalizando
tela.mainloop()
