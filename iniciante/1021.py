def main():
    value = float(input())

    banknotes = [100, 50, 20, 10, 5, 2]
    coins = [100, 50, 25, 10, 5, 1]

    print('NOTAS:')
    for b in banknotes:
        amount = int(value // b)
        value -= b * amount
        print('{} nota(s) de R$ {:.2f}'.format(amount, b))

    value = value * 100

    print('MOEDAS:')
    for c in coins:
        amount = int(value // c)
        value -= c * amount
        print('{} moeda(s) de R$ {:.2f}'.format(amount, c / 100))


if __name__ == '__main__':
    main()
