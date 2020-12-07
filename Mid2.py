# Exercitiul 2

from collections import Counter
lista_nume = ['Maria', 'Irina', 'Claudiu’', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

def sort_by():
    print('Introduce o comanda:')
    print(""" 0 - Sortare alfabetica
              1 - Sortare alfabetica inversa
              2 - Listare dupa numarul de apariti al obiectelor
              """)
    comanda = input(': ')
    if comanda == '0':
        lista_nume.sort()
        print(lista_nume)
    elif comanda == '1':
        lista_nume.sort(reverse=True)
        print(lista_nume)
    elif comanda == '2':
        counts = Counter(lista_nume)
        print(counts)

sort_by()