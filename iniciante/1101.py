def main():
    while True:
        x, y = map(int, input().split())

        if x <= 0 or y <= 0:
            break

        mx, mn = (x, y) if x > y else (y, x)
        l = [n for n in range(mn, mx + 1)]

        print(*l, end=' ')
        print('Sum={}'.format(sum(l)))


if __name__ == '__main__':
    main()
