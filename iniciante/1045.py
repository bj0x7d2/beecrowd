def main():
    values = [float(v) for v in input().split()]

    values.sort(reverse=True)
    a, b, c = values[0], values[1], values[2]

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    else:
        t1 = pow(a, 2)
        t2 = pow(b, 2) + pow(c, 2)
        if t1 < t2:
            print('TRIANGULO ACUTANGULO')
        elif t1 > t2:
            print('TRIANGULO OBTUSANGULO')
        else:
            print('TRIANGULO RETANGULO')

        if a == b and b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or b == c or a == c:
            print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    main()
