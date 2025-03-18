def main():
    n = int(input())

    count = {'in': 0, 'out': 0}

    for _ in range(n):
        number = int(input())
        if number >= 10 and number <= 20:
            count['in'] += 1
        else:
            count['out'] += 1

    print("{} in".format(count['in']))
    print("{} out".format(count['out']))


if __name__ == '__main__':
    main()
