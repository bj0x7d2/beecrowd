def main():
    ray = float(input())

    PI = 3.14159
    volume = 4.0/3.0 * PI * pow(ray, 3)

    print('VOLUME {:.3f}'.format(volume))


if __name__ == '__main__':
    main()