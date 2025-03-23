def main():
    n = int(input())

    for _ in range(n):
        number = int(input())

        p = 'EVEN' if number % 2 == 0 else 'ODD'

        if number == 0:
            print('NULL')
        elif number > 0:
            print('{} POSITIVE'.format(p))
        else:
            print('{} NEGATIVE'.format(p))


if __name__ == '__main__':
    main()
