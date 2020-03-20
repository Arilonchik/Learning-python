def main():
    book = {}
    for _ in range(int(input())):
        comm = input().split()
        if comm[0] == 'add':
            book[comm[1]] = comm[2]
        if comm[0] == 'find':
            try:
                print(book[comm[1]])
            except KeyError:
                print('not found')
        if comm[0] == 'del':
            if comm[1] in book.keys():
                book.pop(comm[1])
###########################################


def hash_f():
    book = [None for _ in range((10**7) + 1)]
    for _ in range(int(input())):
        comm = input().split()
        comm[1] = int(comm[1])
        if comm[0] == 'add':
            book[comm[1]] = comm[2]
        if comm[0] == 'find':
            print(book[comm[1]]or 'not found')
        if comm[0] == 'del':
            book[comm[1]] = None


if __name__ == '__main__':
    hash_f()
