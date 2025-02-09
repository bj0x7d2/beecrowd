def main():
    values = [int(v) for v in input().split()]

    copy = values.copy()
    copy.sort()

    for c in copy:
        print(c)

    print()
    for v in values:
        print(v)


if __name__ == '__main__':
    main()