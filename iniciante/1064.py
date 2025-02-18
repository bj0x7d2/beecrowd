def main():
    sum = 0
    count = 0
    for i in range(6):
        number = float(input())
        if number >= 0:
            sum += number
            count += 1

    average = sum / count
    print('{} valores positivos'.format(count))
    print('{:.1f}'.format(average))


if __name__ == '__main__':
    main()
