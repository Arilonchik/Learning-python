import datetime


def main():
    date = datetime.date(*map(int, input().split()))
    delta = datetime.timedelta(days=int(input()))
    print((date + delta).year, (date + delta).month, (date + delta).day)


if __name__ == '__main__':
    main()
