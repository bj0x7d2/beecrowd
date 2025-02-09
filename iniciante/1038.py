def main():
    code, amount = map(int, input().split())

    price_table = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}

    price = price_table[code] * amount

    print('Total: R$ {:.2f}'.format(price))


if __name__ == '__main__':
    main()