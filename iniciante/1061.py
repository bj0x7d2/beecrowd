def read():
    l = input().split()
    d = int(l[1])
    h, m, s = map(int, input().split(sep=':'))
    return d, h, m, s


def difference(n1, n2, t):
    c = 0
    if n2 >= n1:
        n = n2 - n1
    else:
        n = (t + n2) - n1
        c = - 1

    if n >= t:
        return n - t, 1
    else:
        return n, c


def write(d, h, m, s):
    print('{} dia(s)'.format(d))
    print('{} hora(s)'.format(h))
    print('{} minuto(s)'.format(m))
    print('{} segundo(s)'.format(s))


def main():
    d1, h1, m1, s1 = read()
    d2, h2, m2, s2 = read()

    s, c = difference(s1, s2, 60)
    m, c = difference(m1, m2+c, 60)
    h, c = difference(h1, h2+c, 24)
    d, c = difference(d1, d2+c, pow(2, 31))

    write(d, h, m, s)


if __name__ == '__main__':
    main()
