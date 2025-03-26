def main():
    n = int(input())

    weights = [2, 3, 5]
    for _ in range(n):
        v1, v2, v3 = map(float, input().split())
        average = (v1 * 2 + v2 * 3 + v3 * 5) / 10
        print('{:.1f}'.format(average))


if __name__ == '__main__':
    main()
