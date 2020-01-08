# Napisz funkcję grupuj,
# która będzie grupowała słowniki według wartości dla wybranego klucza.


owoce = [
    {'nazwa': 'jabłko', 'kolor': 'czerwony', 'smak': 'kwaśny'},
    {'nazwa': 'banan', 'kolor': 'żółty', 'smak': 'słodki'},
    {'nazwa': 'cytryna', 'kolor': 'żółty', 'smak': 'kwaśny'},
    {'nazwa': 'gruszka', 'kolor': 'zielony', 'smak': 'słodki'},
    {'nazwa': 'truskawka', 'kolor': 'czerwony', 'smak': 'słodki'}
]


def grupuj(lista_slownikow, klucz):
    nowe_grupy = {}
    watosci_klucza = []

    for slownik in lista_slownikow:
        if not slownik[klucz] in watosci_klucza:
            watosci_klucza.append(slownik[klucz])

    for watosc_klucza in watosci_klucza:
        slowniki_jednej_wartosci = []
        for slownik in lista_slownikow:
            if slownik[klucz] == watosc_klucza and slownik not in slowniki_jednej_wartosci:
                slowniki_jednej_wartosci.append(slownik)
        nowe_grupy[watosc_klucza] = slowniki_jednej_wartosci

    return nowe_grupy


grupy = grupuj(owoce, 'kolor')
for kolor, lista_owocow in grupy.items():
    print(kolor, lista_owocow)

'''
#poniżej wersja z nazwami innymi niż w poleceniu
ale bardziej uniwersalnymi pod każdy klucz:

grupy = grupuj(owoce, 'smak')
for wartosc_wybranego_klucza, slowniki_dla_wartosci in grupy.items():
    print(wartosc_wybranego_klucza, slowniki_dla_wartosci)
'''

input('\nPress enter to exit')
