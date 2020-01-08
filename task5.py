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

input('\nPress enter to exit')
