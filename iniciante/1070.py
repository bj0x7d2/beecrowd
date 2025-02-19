def main ():
    number = int(input())

    s = number if number % 2 != 0 else number + 1
    for n in range(s, s + 12, 2):
        print(n)


if __name__ == '__main__':
    main()