def main():
    count = 0
    for i in range(6):
        number = float(input())
        if number >= 0:
            count += 1

    print('{} valores positivos'.format(count))


if __name__ == '__main__':
    main()
