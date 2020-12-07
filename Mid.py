string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]


def replacer(text1):
    liste = []
    jap = True
    while jap:
        start = 1
        end = 1
        de_inlocuit = input("Introduce textul ce trebuie inlocuit: ")
        alte_lucruri_de_inlocuit = input("Doriti sa inlocuiti si altceva(d/n): ")
        if alte_lucruri_de_inlocuit == "d":
            start = int(input("Index de start: "))
            end = int(input("index de sfarsit: "))
        elif alte_lucruri_de_inlocuit == "n":
            pass
        else:
            print("Va rugam introduceti o comanda valida >>(d/n)")
        lista_temporara = [start, end, de_inlocuit]
        liste.append(lista_temporara)
    lista_de_stringuri = list(text1)

    for lista in liste:
        lista_de_stringuri[lista[0] - 1:lista[1] - 1] = lista[2]
    text_de_modifcat = "".join(lista_de_stringuri)
    return text_de_modifcat


string_modifcat = replacer(string)
print(string_modifcat)