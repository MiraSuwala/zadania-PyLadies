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

input('\nPress enter to exit')
