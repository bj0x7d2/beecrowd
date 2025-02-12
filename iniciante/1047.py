def main():
    h1, m1, h2, m2 = map(int, input().split())

    if h1 < h2:
        h = h2 - h1

        if m1 <= m2:
            m = m2 - m1
        else:
            m = (60 + m2) - m1
            h -= 1
    elif h1 > h2:
        h = (24 + h2) - h1

        if m1 <= m2:
            m = m2 - m1
        else:
            m = (60 + m2) - m1
            h -= 1
    else:
        if m1 < m2:
            h = 0
            m = m2 - m1
        elif m1 > m2:
            h = 23
            m = (60 + m2) - m1
        else:
            h = 24
            m = 0

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))


if __name__ == '__main__':
    main()
