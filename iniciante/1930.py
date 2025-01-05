def calculate():
    sum = 0
    for t in input().split():
        sum += int(t)
    return sum - 3


def main():
    number = calculate()

    print('{}'.format(number))


if __name__ == '__main__':
    main()
