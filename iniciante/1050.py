def main():
    ddd = int(input())

    city = ''
    match ddd:
        case 61:
            city = 'Brasilia'
        case 71:
            city = 'Salvador'
        case 11:
            city = 'Sao Paulo'
        case 21:
            city = 'Rio de Janeiro'
        case 32:
            city = 'Juiz de Fora'
        case 19:
            city = 'Campinas'
        case 27:
            city = 'Vitoria'
        case 31:
            city = 'Belo Horizonte'
        case _:
            city = 'DDD nao cadastrado'

    print(city)


if __name__ == '__main__':
    main()
