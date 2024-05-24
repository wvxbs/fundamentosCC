# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def jogo(sheldon, raj):
    golpes = {"tesoura": ["papel", "lagarto"],"papel": ["pedra", "Spock"],"pedra": ["lagarto", "tesoura"],"lagarto": ["Spock", "papel"],"Spock": ["tesoura", "pedra"]
    }
    respostas = ["Bazinga!", "Raj trapaceou!", "De novo!"]

    if sheldon == raj:
        return respostas[2]
    
    if raj in golpes[sheldon]:
        return respostas[0]
    
    return respostas[1]

def main():
    T = int(input())

    for run in range(T):
        sheldon, raj = input().split(" ")

        R = jogo(sheldon, raj)
        
        print(f"Caso #{run + 1}: {R}")
    
main()      