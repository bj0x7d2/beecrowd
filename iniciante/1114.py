def main():
    while True:
        password = input()

        if password == '2002':
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')


if __name__ == '__main__':
    main()
