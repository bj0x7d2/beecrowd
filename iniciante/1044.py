def is_multiple(a: int, b: int):
    if a > b:
        return a % b == 0
    else:
        return b % a == 0


def main():
    a, b = map(int, input().split())

    if is_multiple(a, b):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


if __name__ == '__main__':
    main()
