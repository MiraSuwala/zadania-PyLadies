import datetime

print('\nZadanie 1: TITLE')
# Napisz funkcję o nazwie title, która będzie działała
# tak jak metoda title na stringu, ale nie używaj tej metody

string_1 = 'terapia DR jsoNA'


def handmade_title(string):
    string = string.lower()
    lower_list = string.split()
    titled_string = ''

    for word in lower_list:
        titled_word = word.replace(word[0], word[0].upper())
        titled_string += titled_word
        titled_string += ' '

    titled_string.rstrip()
    print(titled_string)


handmade_title(string_1)


print('\nZadanie 2: GRUPOWANIE')
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
#poniżej wersja wydruku z nazwami bardziej uniwersalnymi pod każdy klucz:
grupy = grupuj(owoce, 'smak')
for wartosc_wybranego_klucza, slowniki_dla_wartosci in grupy.items():
    print(wartosc_wybranego_klucza, slowniki_dla_wartosci)
'''

print('\nZadanie 3: DELTA COMPRESSION')
# Napisz funkcję delta_compression, która jako argument
# przyjmuje posortowaną listę liczb całkowitych
# i zwróci tę samą listę skompresowaną następującym algorytmem:
#   *Pierwszy element listy wyjściowej jest taki sam jak pierwszy element listy wejściowej.
#   *Każdy następny element listy wyjściowej jest równy różnicy
#    między odpowiadającym mu elementem listy wejściowej a elementem poprzedzającym go

lista_wejsciowa_we_1 = [5, 7, 11, 21, 28, 39]


def delta_compression(lista_wejsciowa_we):
    n = len(lista_wejsciowa_we)
    lista_wyjsciowa_wy = [lista_wejsciowa_we[0]]
    for i in range(1, n):
        lista_wyjsciowa_wy.append(lista_wejsciowa_we[i] - lista_wejsciowa_we[i - 1])
    print(lista_wyjsciowa_wy)


delta_compression(lista_wejsciowa_we_1)


print('\nZadanie 4: SUMY DLA DAT')
# Napisz funkcję grupuj_i_licz,
# która jako argument przyjmie listę dwuelementowych krotek,
# gdzie pierwszy element to data (instancja datetime.date),
# a drugi to liczba całkowita,
# i obliczy sumy tych liczb dla każdego miesiąca jaki występuje wśród tych dat.
# Fnkcja powinna zwrócić słownik,
# gdzie kluczami będą krotki (rok, miesiąc), a wartościami sumy liczb.


daty_1 = [
    (datetime.date(2015, 1, 29), 10),
    (datetime.date(2015, 1, 30), 12),
    (datetime.date(2015, 1, 31), 10),
    (datetime.date(2015, 2, 1), 9),
    (datetime.date(2015, 2, 2), 9)
]


def grupuj_i_licz(daty):
    slownik = {}
    daty_klucze = []

    for data, liczba_dla_daty in daty:
        tupla_rok_miesiac = (data.year, data.month)
        if tupla_rok_miesiac not in daty_klucze:
            daty_klucze.append(tupla_rok_miesiac)

    for rok, miesiac in daty_klucze:
        suma_dla_daty = 0
        for data, liczba_dla_daty in daty:
            if rok == data.year and miesiac == data.month:
                suma_dla_daty += liczba_dla_daty
        tupla_rok_miesiac = (rok, miesiac)
        slownik[tupla_rok_miesiac] = suma_dla_daty

    return slownik


x = grupuj_i_licz(daty_1)
print(x)


print('\nZadanie 5: TNIJ')
# Napisz funkcję tnij, która przyjmie dwa argumenty: tekst oraz liczbę.
# Funkcja powinna zwrócić tekst pocięty na fragmenty (listę),
# każdy o długości takiej jak liczba podana w argumencie.
# Ostatni fragment może być krótszy niż wymagana długość.

przykladowy_tekst = '12345678982369826948623649'
przykladowa_liczba = 4


def tnij(tekst, liczba):
    dlugosc_tekstu = len(tekst)

    if liczba >= dlugosc_tekstu:
        fragmenty_pociete = [tekst]
        return fragmenty_pociete
    if liczba <= 0 or type(liczba) != int:
        print('Ta funkcja działa tylko na liczbach całkowitych większych od zera')
        # raise Exception('Ta funkcja działa tylko na liczbach całkowitych większych od zera')
    else:
        if dlugosc_tekstu // liczba:
            liczba_wycinkow = dlugosc_tekstu // liczba + 1
        else:
            liczba_wycinkow = dlugosc_tekstu // liczba

        fragmenty = [tekst]*liczba_wycinkow
        fragmenty_pociete = []
        indeks_wycinka = 0

        for wycinek in fragmenty:
            punkt_odniesienia = liczba * (indeks_wycinka + 1)
            wycinek = wycinek[punkt_odniesienia - liczba: punkt_odniesienia]
            fragmenty_pociete.append(wycinek)
            indeks_wycinka += 1
            
        return fragmenty_pociete


print(tnij(przykladowy_tekst, przykladowa_liczba))


print('\nZadanie 6: POLICZONE SLOWA')
# Napisz funkcję, która jako argument przyjmie dowolny tekst i zwróci słownik,
# którego kluczami będą wszystkie słowa z tego tekstu,
# a wartościami będą liczby wystąpień tych słów w tekście.
# Funkcja powinna być obojętna na wielkość liter (czyli 'Kot' i 'kot' mają
# być traktowane jako jedno słowo) i powinna ignorować znaki interpunkcyjne.

przykladowy_tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
                    "Integer sollicitudin ultricies eros, vitae eleifend ipsum " \
                    "sodales ut. Pellentesque libero ipsum, euismod eget volutpat " \
                    "nec, hendrerit vel turpis."


def licz_slowa(tekst):
    tekst = tekst.lower()
    tekst_podzielony = tekst.split()
    znaki_interpunkcyjne = [' ', ',', '.', ':', ';', '-', '?', '!', '/', '(', ')']
    slowa = []
    policzone_slowa = {}

    for slowo in tekst_podzielony:
        for i in znaki_interpunkcyjne:
            slowo = slowo.strip(i)
        if slowo not in slowa:
            slowa.append(slowo)

    for slowo in slowa:
        policzone_slowa[slowo] = tekst.count(slowo)

    return policzone_slowa


print(licz_slowa(przykladowy_tekst))


input('\nPress enter to exit')
