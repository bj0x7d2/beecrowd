def is_triangle(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def main():
    a, b, c = map(float, input().split())

    if is_triangle(a, b, c):
        perimeter = a + b + c
        print('Perimetro = {:.1f}'.format(perimeter))
    else:
        area = 0.5 * (a + b) * c
        print('Area = {:.1f}'.format(area))


if __name__ == '__main__':
    main()
