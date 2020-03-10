import itertools


def primes():
    prime = 0
    while True:
        flag = 0
        prime += 1
        for x in range(1, prime):
            if not prime % x:
                flag += 1
        if flag == 1:
            yield prime


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]