import csv
from collections import Counter
import re


def main():
    with open("Crimes.csv", 'r') as fh:
        crimes_dict = csv.DictReader(fh)
        c = Counter()
        for row in crimes_dict:
            if re.match(r'\d\d/\d\d/2015', row["Date"]):
                c[row["Primary Type"]] += 1
        print(c.most_common(2))


if __name__ == '__main__':
    main()
