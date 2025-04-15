def main():
    while True:
        x, y = map(int, input().split())

        if x > 0 and y > 0:
            q = 'primeiro'
        elif x < 0 and y > 0:
            q = 'segundo'
        elif x < 0 and y < 0:
            q = 'terceiro'
        elif x > 0 and y < 0:
            q = 'quarto'
        else:
            break

        print(q)


if __name__ == '__main__':
    main()
