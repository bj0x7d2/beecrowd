import math


def read_point():
    x, y = input().split()
    return float(x), float(y)


def calculate_distance(x1, x2, y1, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def main():
    x1, y1 = read_point()
    x2, y2 = read_point()

    dist = calculate_distance(x1, x2, y1, y2)

    print('{:.4f}'.format(dist))


if __name__ == '__main__':
    main()
