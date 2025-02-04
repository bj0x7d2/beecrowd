def main():
    a, b, c = map(int, input().split())

    maxAB = (a + b + abs(a - b)) / 2
    maxABC = (c + maxAB + abs(c - maxAB)) / 2

    print('{} eh o maior'.format(int(maxABC)))


if __name__ == '__main__':
    main()
