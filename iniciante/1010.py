def calculate_price():
    _, amount, price = input().split()
    return int(amount) * float(price)


def main():
    price_one = calculate_price()
    price_two = calculate_price()

    total_price = price_one + price_two

    print('VALOR A PAGAR: R$ {:.2f}'.format(total_price))


if __name__ == '__main__':
    main()
