from math import sqrt
from re import compile, search

def zadanie1():
    print('Zadanie 1\n')
    letter = input('Podaj literę: ')
    vowel = ('a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y')
    consonants = ('q', 'w', 'r', 't', 'p', 's', 'd', 'f',
                  'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
                  'v', 'b', 'n', 'm', 'ł', 'ż', 'ź', 'ś', 'ć')

    if letter in vowel:
        print('Litera jest samogłoską')
    elif letter in consonants:
        print('Litera jest spółgłoską')
    else:
        print('Nie ma takiej litery w języku polskim')

def zadanie2():
    print('Zadanie 2\n')
    number = int(input('Podaj liczbę: '))
    if number % 2 == 0:
        print('Liczba jest parzysta\n')
    else:
        print('Liczba jest nieparzysta\n')

    print("Sprawdzenie bez instrukcji if:")
    result = ('Liczba jest parzysta', 'Liczba jest nieparzysta')
    print(result[number % 2])

def zadanie3():
    print('Zadanie 3\n')
    print('Rozwiązywanie równania w postaci ax^2+bx+c=0')
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))

    if a == 0:
        print('Równanie nie jest kwadratowe')
    else:
        delta = (b**2) - (4 * a * c)
        if delta < 0:
            print("Równanie nie ma rozwiązania w zbiorze liczb rzeczywistych")
        elif delta == 0:
            result = (-b)/(2*a)
            print('Rozwiązanie równania: %s' % result)
        else:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            print('Rozwiązaniami równania są: %s i %s' % (x1, x2))

def zadanie4():
    print('Zadanie 4\n')
    print('''
    *            *        ****
    *           * *       *   *
    *          *   *      *   *
    *         *******     ****
    *        *       *    * *
    *       *         *   *  *
    *****  *           *  *   *
    ''')

def zadanie5():
    print('Zadanie 5\n')
    password = input('Wpisz hasło: ')
    reg = compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d@$#%*?&!]{6,16}$')
    if search(reg, password):
        print("Hasło spełnia wymagania")
    else:
        print("Hasło nie spełnia wymagań")

def zadanie6():
    print('Zadanie 6\n')
    numberI = int(input('Podaj liczbę: '))
    if numberI > 0:
        print(' ', end=' ')

        for i in range(1, numberI + 1):
            strI = str(i)
            print(strI.rjust(6), end=' ')
        print()

        for j in range(1, 11):
            print(str(j).rjust(2), end='')
            for i in range(1, numberI + 1):
                result = str(i * j)
                print(result.rjust(6), end=' ')
            print()
    else:
        print('Liczba musi być większa od 0!')

def zadanie7():
    print('Zadanie 7\n')
    n = int(input('Podaj liczbę: '))
    if n == 0:
        print('Wartość dla 0 miejsca jest równa 0.')
    elif n == 1:
        print('Wartość dla 1 miejsca jest równa 1.')
    elif n > 1:
        n0 = 0
        n1 = 1
        i = 1
        while i < n:
            n0 += n1
            i += 1
            if i >= n:
                break
            n1 += n0
            i += 1
        result = max(n0, n1)
        print('Wartość dla %s miejsca jest równa %s.' % (n, result))
    else:
        print('Liczba musi być większa bądź równa 0!')

def zadanie8():
    print('Zadanie 8\n')
    for number in range(1, 10):
        print(str(number) * number)

def zadanie9():
    print('Zadanie 9\n')
    m = int(input('Podaj liczbę wierszy: '))
    n = int(input('Podaj liczbę kolumn: '))
    listNumber = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            listNumber[i][j] = i*j

    for line in listNumber:
        for num in line:
            print(num, end=' ')
        print()

def zadanie10():
    print('Zadanie 10\n')
    listNumber = []
    for number in range(100, 401):
        num = str(number)
        if '1' in num or '3' in num or '5' in num or '7' in num or '9' in num:
            continue
        listNumber.append(num)

    for l in listNumber:
        print(l, end=', ')

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