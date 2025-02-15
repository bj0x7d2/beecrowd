def main():
    w1 = input()
    w2 = input()
    w3 = input()

    table = {
        0: 'minhoca',
        1: 'sanguessuga',
        2: 'lagarta',
        3: 'pulga',
        4: 'vaca',
        5: 'homem',
        6: 'aguia',
        7: 'pomba',
    }

    key = 0b000

    if w1 == 'vertebrado':
        key |= 0b100
        if w3 == 'onivoro':
            key |= 0b001
    else:
        if w3 == 'hematofago':
            key |= 0b001

    if w2 == 'ave' or w2 == 'inseto':
        key |= 0b010

    print(table[key])


if __name__ == '__main__':
    main()
