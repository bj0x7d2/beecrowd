def main():
    n = int(input())

    for _ in range(n):
        x, y = map(int, input().split())

        mx, mn = (x, y) if x > y else (y, x)
        mn = mn + 2 if mn % 2 != 0 else mn + 1

        s = 0
        for k in range(mn, mx, 2):
            s += k

        print('{}'.format(s))


if __name__ == '__main__':
    main()
