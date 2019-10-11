from math import sin, pi

def zadanie1():
    a = input()
    b = input()
    suma = a + b
    print(suma)

def zadanie2():
    a = 3
    b = 4
    alfa = 47
    result = 0.5 * a * b * round(sin(alfa * pi / 180), 4)
    print(round(result, 4))

if __name__ == '__main__':
    zadanie1()
    zadanie2()