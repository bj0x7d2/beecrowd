def main():
    value = float(input())

    match value:
        case _ as v if v >= 0 and v <= 25:
            print('Intervalo [0,25]')
        case _ as v if v > 25 and v <= 50:
            print('Intervalo (25,50]')
        case _ as v if v > 50 and v <= 75:
            print('Intervalo (50,75]')
        case _ as v if v > 75 and v <= 100:
            print('Intervalo (75,100]')
        case _:
            print('Fora de intervalo')


if __name__ == '__main__':
    main()
