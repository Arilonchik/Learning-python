import sys
import re


def find_cat():
    for line in sys.stdin:
        line = line.rstrip()
        if len(re.findall(r'cat', line)) >= 2:
            print(line)


def find_self_cat():
    for line in sys.stdin:
        line = line.rstrip()
        if re.match(r'.*\bcat\b.*', line):
            print(line)


def find_z():
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'z.{3}z', line):
            print(line)


def find_backslash():
    sys.stdout.writelines(filter(re.compile(r'\\').search, sys.stdin))


def find_tandem():
    sys.stdout.writelines(filter(re.compile(r'\b(.+)\1\b').search, sys.stdin))


def change_human():
    sys.stdout.writelines(map(lambda x: re.sub(r'human', 'computer', x), sys.stdin))
    print(re.sub(r'human', 'computer', sys.stdin.read()), end='')


def change_a():
    sys.stdout.writelines(map(lambda x: re.sub(r'\ba+\b', 'argh', x, flags=re.IGNORECASE, count=1), sys.stdin))


def change_let():
    for line in sys.stdin:
        print(re.sub(r'\b(\w?)(\w?)', r'\2\1', line), end='')


def change_same():
    for line in sys.stdin:
        print(re.sub(r'(\w?)\1*', r'\1', line), end='')


def some_task():
    for line in sys.stdin:
        line = line.rstrip()
        if re.fullmatch(r'[01]+', line):
            ans = 0
            for i in range(len(line)):
                if i % 2 == 0:
                    ans += int(line[i])
                else:
                    ans -= int(line[i])
            if ans % 3 == 0:
                print(line)


if __name__ == '__main__':
    some_task()
