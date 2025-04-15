def main():
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())

        try:
            r = float(x) / y
            print('{:.1f}'.format(r))
        except:
            print('divisao impossivel')


if __name__ == '__main__':
    main()
