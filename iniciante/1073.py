def main():
    n = int(input())

    n = n if n % 2 != 0 else n + 1

    for i in range(2, n, 2):
        print('{}^2 = {}'.format(i, i**2))


if __name__ == '__main__':
    main()
