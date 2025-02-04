def main():
    value = int(input())
    values = [100, 50, 20, 10, 5, 2, 1]

    print('{}'.format(value))

    for v in values:
        amount = value // v
        value -= v * amount
        print('{} nota(s) de R$ {},00'.format(amount, v))


if __name__ == '__main__':
    main()
