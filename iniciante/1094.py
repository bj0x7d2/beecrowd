def main():
    n = int(input())

    c, r, s = (0, 0, 0)
    for _ in range(n):
        a, t = input().split()
        match t:
            case 'C':
                c += int(a)
            case 'R':
                r += int(a)
            case 'S':
                s += int(a)

    total = c + r + s

    print('Total: {} cobaias'.format(total))
    print('Total de coelhos: {}'.format(c))
    print('Total de ratos: {}'.format(r))
    print('Total de sapos: {}'.format(s))
    print('Porcentual de coelhos: {:.2f}'.format(c / total * 100))
    print('Porcentual de ratos: {:.2f}'.format(r / total * 100))
    print('Porcentual de sapos: {:.2f}'.format(s / total * 100))


if __name__ == '__main__':
    main()
