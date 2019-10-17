from math import sin, pi, floor
from cmath import sqrt, sin as sinz, cos
from numpy import angle, conjugate, real, imag
import builtins

def zadanie1():
    print('Zadanie 1: ')
    a = input()
    b = input()
    suma = a + b
    print(suma + '\n')
    '''Funkcja input pobiera wartości w formie ciągu znaków
    więc zmienna b jest dopisana do końca zmiennej a'''

def zadanie2():
    a = 3
    b = 4
    alfa = 47
    result = 0.5 * a * b * round(sin(alfa * pi / 180), 4)
    print('Zadanie 2: ')
    print('%s \n' % round(result, 4))

def zadanie3():
    print('Zadanie 3: ')
    a = int(input('Pierwszy bok: '))
    b = int(input('Drugi bok: '))
    alfa = int(input('Kąt między bokami: '))
    result = 0.5 * a * b * round(sin(alfa * pi / 180), 4)
    print('%s \n' % round(result, 4))

def zadanie4():
    print('Zadanie 4: ')
    print(dir(builtins))
    print(help(print))
    print('Ala ma kota')
    print(2 + 2)
    print('%s\t%s\t%s\t%s' % (2**5, 35//2, 35/2, 35%2))
    print('%s\n%s\n%s\n%s' % (2**5, 35//2, 35/2, 35%2))

def zadanie5():
    print('Zadanie 5: ')
    print('5 // 2: %s' % (5 // 2))
    print('Operacja 5 // 2 zwraca liczbe całkowitą bez reszty\n')

    print('round(5 / 2): %s' % (round(5 / 2)))
    print('round(2.6): %s' % (round(2.6)))
    print('Funkcja round() zwraca najbliższą liczbę całkowitą\n')

    print('floor(5 / 2): %s' % (floor(5 / 2)))
    print('floor(2.6): %s' % (floor(2.6)))
    print('Funkcja floor zaorągla liczbę w dół do liczby całkowitej')

def zadanie6():
    print('Zadanie 6: ')
    print(sqrt(complex(-17)))

def zadanie7():
    print('Zadanie 7: ')
    print('Zmienna _ w trybie interaktywnym służy do zapisywania')
    print('ostatnio podanej wartości, np:')
    print('>>> 10')
    print('10')
    print('>>> _ ** 2')
    print('100')

def zadanie8():
    print('Zadanie 8: ')
    a = int(input('Podaj liczbę a: '))
    b = int(input('Podaj liczbę b taką że b < a: '))

    if b < a:
        Z = b % a
        Z *= Z + 3
        print(Z)
    else:
        print('Podano złe b!')

def zadanie9():
    print('Zadanie 9: ')
    z = complex(input('Podaj liczbę: '))
    print(abs(z))
    print(angle(z))
    print(conjugate(z))

def zadanie10():
    print('Zadanie 10: ')
    z = complex(0, 1)
    zsin = sinz(z)
    zcos = cos(z)

    print('Część rzeczywista z sin(i): %s' % zsin.real)
    print('Część urojona z sin(i): %s' % zsin.imag)

    print('Część rzeczywista z cos(i): %s' % zcos.real)
    print('Część urojona z cos(i): %s' % zcos.imag)

    print('\nZależność jest spełniona: ')
    print(sinz(z)**2 + cos(z)**2)

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