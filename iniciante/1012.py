def main():
    a, b, c = map(float, input().split())

    area_triangle = 0.5 * a * c
    area_circle = 3.14159 * c * c
    area_trapezoid = 0.5 * (a + b) * c
    area_square = b * b
    area_rectangle = a * b

    print('TRIANGULO: {:.3f}'.format(area_triangle))
    print('CIRCULO: {:.3f}'.format(area_circle))
    print('TRAPEZIO: {:.3f}'.format(area_trapezoid))
    print('QUADRADO: {:.3f}'.format(area_square))
    print('RETANGULO: {:.3f}'.format(area_rectangle))


if __name__ == '__main__':
    main()
