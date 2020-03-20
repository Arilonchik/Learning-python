from collections import deque


def hash_function(m, s):
    x = 263
    p = 1000000007
    hash_value = 0
    for i in range(len(s)):
        hash_value += (ord(s[i])*x**i)
        hash_value = hash_value % p
    return hash_value % m


def find(tab, str, h_val):
    if str in tab[h_val]:
        return 'yes'
    return 'no'


def main():
    m = int(input())
    h_table = [deque() for _ in range(m)]
    for _ in range(int(input())):
        req, val = input().split()
        hash_val = hash_function(m, val)
        if req == 'find':
            print(find(h_table, val, hash_val))
        if req == 'add':
            if find(h_table, val, hash_val) == 'no':
                h_table[hash_val].appendleft(val)
        if req == 'del':
            if find(h_table, val, hash_val) == 'yes':
                h_table[hash_val].remove(val)
        if req == 'check':
            print(' '.join(h_table[int(val)]))


if __name__ == '__main__':
    main()
