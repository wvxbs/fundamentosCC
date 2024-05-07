def main():
    frase = input()
    frase_ = ""
    i = 0
    while i < len(frase):
        match frase[i]:
            case "@": frase_ += ("a")
            case "&": frase_ += ("e")
            case "!": frase_ += ("i")
            case "*": frase_ += ("o")
            case "#": frase_ += ("u")
            case _: frase_ += (frase[i])
        i +=1
    print(frase_)

main()