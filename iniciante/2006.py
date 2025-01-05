def count_answer():
    correct = input()
    count = 0
    for answer in input().split():
        if answer == correct:
            count += 1
    return count


def main():
    number = count_answer()

    print('{}'.format(number))


if __name__ == '__main__':
    main()
