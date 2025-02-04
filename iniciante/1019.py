def main():
    time = int(input())

    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    hours = time // SECONDS_PER_HOUR
    time -= hours * SECONDS_PER_HOUR
    minutes = time // SECONDS_PER_MINUTE
    time -= minutes * SECONDS_PER_MINUTE
    seconds = time

    print('{}:{}:{}'.format(hours, minutes, seconds))


if __name__ == '__main__':
    main()
