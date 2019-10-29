from numpy import prod
from math import pi, factorial
from itertools import permutations
from sys import argv
from colorsys import rgb_to_hsv

def zadanie1():
    print('Zadanie 1\n')
    if len(argv) > 1:
        my_list = argv[1:]
        my_list = list(map(int, my_list))

        print('Suma elementów listy: %s' % sum(my_list))
        print('Iloczyn elementów listy: %s' % prod(my_list))
    else:
        print('Nie podano listy')

def delete(myList):
    newList = []
    for m in myList:
        if m not in newList:
            newList.append(m)
    return newList

def zadanie2():
    print('Zadanie 2\n')
    if len(argv) > 1:
        my_list = argv[1:]
        newList = delete(my_list)
        print(newList)
    else:
        print('Nie podano listy')

def stopnieRadiany(num):
    return num * pi / 180

def radianyStopnie(num):
    return num * 180 / pi

def zadanie3():
    print('Zadanie 3\n')
    choice = int(input('Konwertowanie stopni na radiany wpisz 1\n'
                       'konwertowanie radianów na stopnie wpisz 2: '))
    number = int(input('Podaj wartość: '))

    if choice == 1:
        print(stopnieRadiany(number))
    elif choice == 2:
        print(radianyStopnie(number))
    else:
        print('Nie ma takiej opcji!')

def calc(n , a = 1, q = 2):
    i = 2
    while i <= n:
        a *= q
        i += 1
    return a

def zadanie4():
    print('Zadanie 4\n')
    while True:
        n = int(input('Podaj numer elementu ciągu: '))
        if n >= 1:
            break
        else:
            print('Liczba musi być większa od 0')

    a1 = int(input('Wartość pierwszego elementu ciągu: '))
    q = int(input('Wartość ciągu geometrycznego: '))

    print(calc(n, a1, q))

def zadanie5():
    print('Zadanie 5\n')
    if len(argv) > 1:
        myList = argv[1:]
        myList = list(map(int, myList))
        for per in list(permutations(myList)):
            print(per)
    else:
        print('Nie podano listy')

def zadanie6():
    print('Zadanie 6\n')
    r = int(input('Podaj liczbę r: '))
    g = int(input('Podaj liczbę g: '))
    b = int(input('Podaj liczbę b: '))
    print('HSV: %s, %s, %s' % rgb_to_hsv(r, g, b))

def zadanie7():
    print('Zadanie 7\n')

    number = int(input('Podaj liczbę wierszy: '))

    if number >= 1:
        result = []
        for num in range(number):
            row = []
            for element in range(num + 1):
                row.append(int((factorial(num)) / ((factorial(element)) * factorial(num - element))))
            result.append(row)

        for row in result:
            for r in row:
                print(r, end=' ')
            print()
    else:
        print('Podano nie prawidłową liczbę wierszy!')

def zadanie8():
    print('Zadanie 8\n')
    number = int(input('Podaj liczbę: '))
    if number > 0:
        result = 0
        for n in range(1, number + 1):
            result += 1 / (n)
        print(result)
    else:
        print('Podano złą wartość')

def zadanie9():
    print('Zadanie 9\n')
    while True:
        number = int(input('Podaj liczbę całkowitą większą od 0: '))
        if number > 0:
            print(factorial(number))
            break
        else:
            print('Liczba jest za małą')

def euklides(a, b):
    if a == 0 or b == 0:
        number = max(a, b)
        print('Największy wspólny dzielnik to %s' % number)
    else:
        euklides((b % a), a)

def zadanie10():
    print('Zadanie 10\n')
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj pierwszą liczbę: '))

    if a >= 0 and b >= 0:
        euklides(a, b)
    else:
        print('Podano złe wartości.')

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