def main():
    x = int(input())
    y = int(input())

    (mx, mn) = (x, y) if x > y else (y, x)

    mn = mn + 1 if mn % 2 == 0 else mn + 2

    r = sum(range(mn, mx, 2))

    print(r)


if __name__ == '__main__':
    main()
