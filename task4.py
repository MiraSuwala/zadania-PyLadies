import datetime

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


input('\nPress enter to exit')
