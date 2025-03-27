def main():

    maximum = int(input())
    position = 1
    for i in range(1, 100):
        number = int(input())
        if number > maximum:
            maximum = number
            position = i + 1

    print('{}'.format(maximum))
    print('{}'.format(position))


if __name__ == '__main__':
    main()
