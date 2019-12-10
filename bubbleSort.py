from random import randrange

def bubble_sort(numbers):
    n = len(numbers)
    while n > 1:
        for i in range(n-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        n -= 1
    print(numbers)

def main():
    numbers = []
    for i in range(1000):
        numbers.append(randrange(1, 100))
    print(numbers)
    bubble_sort(numbers)

if __name__ == '__main__':
    main()