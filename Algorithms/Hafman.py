import collections
from collections import Counter, namedtuple
import heapq


# not mine
def popmin(tree, codes, num):
    el = tree.pop(tree.index(min(tree)))
    for s in el[1]:
        codes[s] = num + codes[s]
    return el[0], el[1]


def main():
    sss = input().strip()
    count = collections.Counter(sss)
    codes = dict.fromkeys(count, '0' if len(count) == 1 else '')
    tree = [[count[key], key] for key in count]
    while len(tree) > 1:
        val1, s1 = popmin(tree, codes, '0')
        val2, s2 = popmin(tree, codes, '1')
        tree.append([val1 + val2, s1 + s2])
    word = ''.join(codes[s] for s in sss)
    print(len(count), len(word))
    [print('{}: {}'.format(k, codes[k])) for k in sorted(codes)]
    print(word)
# mine


def get_code(code):
    for key in code.keys():
        if len(key) > 1:
            for l in key:
                code[l] = code[key] + code[l]
    return code


def hafman2():
    s = str(input())
    unic_s = set(s)
    qletters = []
    code = {}
    for let in unic_s:
        a = [let, s.count(let)]
        qletters.append(a)
    if len(qletters) == 1:
        print(1, len(s))
        print(f'{s[0]}: 0')
        print('0'*len(s))
        return
    while len(qletters) != 2:
        min1 = (min(qletters, key=lambda unit: unit[1]))
        qletters.remove(min1)
        min2 = (min(qletters, key=lambda unit: unit[1]))
        qletters.remove(min2)
        code[min1[0]] = '0'
        code[min2[0]] = '1'
        qletters.append([min1[0]+min2[0], min1[1]+min2[1]])
    min1 = (min(qletters, key=lambda unit: unit[1]))
    qletters.remove(min1)
    min2 = qletters[0]
    qletters.remove(min2)
    code[min1[0]] = '0'
    code[min2[0]] = '1'
    qletters.append([min1[0] + min2[0], min1[1] + min2[1]])
    encode = get_code(code)
    coded = ''
    for let in s:
        coded += encode[let]
    print(len(unic_s), len(coded))
    for let in unic_s:
        print(f'{let}: {encode[let]}')
    print(coded)
###########################


def decode(coded, code):
    # unic, count = input().split(' ')
    # codes = {}
    # for i in range(int(unic)):
    #     let_num = input().split(': ')
    #     codes[let_num[1]] = let_num[0]  # let_num[1] - code, [0] - letter
    # coded = input()
    codes = {v: k for k, v in code.items()}
    s = ''
    k = ''
    for num in coded:
        k += num
        if k in codes.keys():
            s += codes[k]
            k = ''
    return s


# Практика
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    Counter(s)  # Посчитать сколько раз в строке встретился каждый символ
    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]   # Первая реализация с генератором, отказываемся
    # из-за проблем со сравнением
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1,  left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h     # После выхода из цикла очередь будет иметь такой вид
        root.walk(code, '')
    return code


def main2():
    s = input()
    code = huffman_encode(s)
    print(code)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


def test(n_iter = 100):
    import random
    import string
    for i in range(n_iter):
        lenght = random.randint(0, 32)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(lenght))
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        assert decode(encoded, code) == s


if __name__ == '__main__':
    test()
