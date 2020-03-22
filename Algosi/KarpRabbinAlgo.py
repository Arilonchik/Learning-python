from collections import deque


def hash_f(txt, last=None, prev_let=None):
    x = 263
    p = 1000000007
    if last:
        hash_value = ((last-ord(prev_let)*x**(len(txt)-1))*x + ord(txt[0])) % p
        hash_value = (hash_value + p) % p
         # hash_value = ((last % p - ord(prev_let) * x ** (len(txt) - 1) % p) % p * x) + (ord(txt[0]) % p)
    else:
        hash_value = 0
        for i in range(len(txt)):
            hash_value += (ord(txt[i])*x**i) % p
            # hash_value += (ord(txt[i]) * pow(x, i, p)) % p
    return hash_value


def main():
    pattern = input()
    text = input()
    que = deque([i for i in (text[-len(pattern):])])
    joins = []
    pat_hash = hash_f(pattern)
    if ''.join(que) == pattern:
        joins.append(len(text) - len(pattern))
    prev_hash = hash_f(''.join(que))
    count = len(text) - len(pattern)
    for t in reversed(text[:-len(pattern)]):
        count -= 1
        prev_let = que.pop()
        que.appendleft(t)
        current_hash = hash_f(''.join(que), prev_hash, prev_let)
        if current_hash == pat_hash:
            if ''.join(que) == pattern:
                joins.append(count)
        prev_hash = current_hash
    print(' '.join(map(str, joins[::-1])))

import sys


def easy_hash():
    pattern = sys.stdin.readline().rstrip()
    text = sys.stdin.readline().rstrip()
    pat_hash = 0
    for p in pattern:
        pat_hash += ord(p)
    # que = deque([i for i in text[:len(pattern)]])
    que = text[:len(pattern)]
    joins = ''
    # if ''.join(que) == pattern:
    if que == pattern:
        joins += '0 '
    prev_hash = 0
    for s in que:
        prev_hash += ord(s)
    count = 0
    for t in text[len(pattern):]:
        count += 1
        prev_let = que[0]
        que = que[1:] + t
        current_hash = prev_hash - ord(prev_let) + ord(t)
        if current_hash == pat_hash:
            fl = True
            for s in range(len(que)):
                if que[s] != pattern[s]:
                    fl = False
                    break
            if fl:
                joins += str(count) + ' '
        prev_hash = current_hash
    print(joins)
####################################
#stole#


def Rabin_Karp_Matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):  # preprocessing
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(n - m + 1):  # note the +1
        if p == t:  # check character by character
            print(str(s), end=' ')
        if s < n - m:
            t = (t - h * ord(text[s])) % q  # remove letter s
            t = (t * d + ord(text[s + m])) % q  # add letter s+m
            t = (t + q) % q  # make sure that t >= 0


def main2():
    pattern = sys.stdin.readline().rstrip()
    text = sys.stdin.readline().rstrip()
    Rabin_Karp_Matcher(text, pattern, 257, 2**31-1)


if __name__ == '__main__':
    main2()
