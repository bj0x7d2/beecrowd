def main():
    n = int(input())

    for i in range(1, 11):
        r = i * n
        print('{} x {} = {}'.format(i, n, r))

if __name__ == '__main__':
    main()
