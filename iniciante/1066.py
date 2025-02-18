def main():
    even, odd = 0, 0
    pos, neg = 0, 0

    for _ in range(5):
        number = int(input())

        if number % 2 == 0:
            even += 1
        else:
            odd += 1

        if number > 0:
            pos += 1
        elif number < 0:
            neg += 1

    print(f'{even} valor(es) par(es)')
    print(f'{odd} valor(es) impar(es)')
    print(f'{pos} valor(es) positivo(s)')
    print(f'{neg} valor(es) negativo(s)')


if __name__ == '__main__':
    main()
