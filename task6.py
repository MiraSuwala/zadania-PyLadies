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
