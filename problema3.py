def main():
    simbolos = "A, B, C, D, E, F, Z, H, I, K, L, M, N, O, P, Q, R, S, T, V, X"
    frase = "rkrkrkbsss"

    print(codificar(simbolos.lower(), frase.lower(), 12))

def definirIndiceDoCaractere(letra, simbolos):
    i = 0
    while i < len(simbolos):
        if letra == simbolos[i]:
            return i
        i += 1

def codificar(simbolos, frase, chave):
    fraseDecodificada = []
    simbolos = simbolos.split(", ")    
    i = 0

    for letra in frase:
        fraseDecodificada.append(simbolos[definirIndiceDoCaractere(letra, simbolos) - chave])
    
    fraseDecodificada = "".join(str(i) for i in fraseDecodificada)
    return fraseDecodificada

main()