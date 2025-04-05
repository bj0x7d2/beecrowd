def main():
    for i in range(0, 21, 2):
        for j in range(1, 4):
            k = i / 10
            print('I={:.2g} J={:.2g}'.format(k, j + k))


if __name__ == '__main__':
    main()
