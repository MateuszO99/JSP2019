from math import exp
from itertools import chain

def zadanie1():
    print('Zadanie 1:')
    for i in range(1, 20):
        print(1.2 * exp(1) + 3 + 34.5)

def zadanie2():
    print('Zadanie 2:')
    word = input('Wprowadź napis: ') + '\n'
    print(word * 30)

def zadanie3():
    print('Zadanie 3:')
    word = input('Wprowadź napis: ')
    new_word = word[:2] + word[-2:]
    print(new_word)

def zadanie4():
    print('Zadanie 4:')
    word = input('Wprowadź napis: ')
    new_word = ''

    for letter in range(len(word)):
        if letter == 0:
            new_word += word[0]
            continue
        elif word[letter] == word[0].lower():
            new_word += '$'
        else:
            new_word += word[letter]
    print(new_word)

def zadanie5():
    print('Zadanie 5:')
    word = input('Wprowadź napis: ')
    length = int(len(word) / 2)
    new_word = word[:length] + 'Python' + word[length:]
    print(new_word)

def zadanie6():
    students = ['Kasia', 'Basia', 'Marek', 'Darek']
    students.append('Józek')
    students.extend(['Ania', 'Basia'])
    students.sort()

    print(students[3])
    print(students[:2])
    print(students[-2:])

    while 'Basia' in students:
        students.remove('Basia')

    print(len(students))

    students2 = tuple(students)
    print(type(students2))

def zadanie7():
        my_list = [(2, 8), (5, 5), (9, 3), (1, 0),(3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
        my_list = sorted(my_list, key=lambda my_l: my_l[1])
        print(my_list)

def zadanie8():
    my_list = ['M', 'a', 't', 'e', 'u', 's', 'z']
    word = ''.join(my_list)
    print(word)

def zadanie9():
    new_list = list(chain([2, 4, 3], [1, 5, 6], [9], [7, 9, 0]))
    print(new_list)

def zadanie10():
    my_list = []
    for number in range(3, 100, 3):
        my_list.append(number)

    for num in range(4, len(my_list), 2):
        try:
            del my_list[num]
        except:
            break

    result = sum(my_list) / len(my_list)
    print(result)

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 10!')

    if exercise == 1:
        zadanie1()
    elif exercise == 2:
        zadanie2()
    elif exercise == 3:
        zadanie3()
    elif exercise == 4:
        zadanie4()
    elif exercise == 5:
        zadanie5()
    elif exercise == 6:
        zadanie6()
    elif exercise == 7:
        zadanie7()
    elif exercise == 8:
        zadanie8()
    elif exercise == 9:
        zadanie9()
    elif exercise == 10:
        zadanie10()

    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()