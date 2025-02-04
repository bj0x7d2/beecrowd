def main():
    time = int(input())
    speed = int(input())

    distance = speed * time
    fuel = distance / 12

    print('{:.3f}'.format(fuel))


if __name__ == '__main__':
    main()
