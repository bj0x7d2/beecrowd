def main():
    n1, n2, n3, n4 = map(float, input().split())

    a = (2 * n1 + 3 * n2 + 4 * n3 + n4) / 10

    print('Media: {:.1f}'.format(a))
    if a >= 7:
        print('Aluno aprovado.')
    elif a < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        n5 = float(input())
        print('Nota do exame: {:.1f}'.format(n5))
        a = (n5 + a) / 2
        if a >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(a))


if __name__ == '__main__':
    main()
