import math


def main():
    a, b, c = map(float, input().split())

    d = (b * b) - (4.0 * a * c)
    if a != 0 and d >= 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print('R1 = {:.5f}'.format(r1))
        print('R2 = {:.5f}'.format(r2))
    else:
        print('Impossivel calcular')


if __name__ == '__main__':
    main()
