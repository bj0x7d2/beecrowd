def main():
    distance = int(input())
    fuel = float(input())

    mean = distance / fuel

    print('{:.3f} km/l'.format(mean))


if __name__ == '__main__':
    main()
