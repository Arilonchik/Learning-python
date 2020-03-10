import sys
import heapq    # Реализация кучи
from random import randint
from timing import timed

dots = []


def dots_val(otr):
    dot = otr[0][1]
    dots.append(dot)
    i = 0
    pas = True
    while pas:
        if len(otr) == 0:
            return
        if len(otr) == i != 0:
            i = i-1
        if otr[i][0] <= dot <= otr[i][1]:
            otr.remove(otr[i])
        elif i < len(otr)-1:
            i = i + 1
    if otr:
        dots_val(otr)
    else:
        return


def getKey(item):
    return item[1]

def greedy1():
    count = int(input())
    otr = []
    for i in range(count):
        a, b = map(int, input().split())
        o = [min(a, b), max(a, b)]
        otr.append(o)
    otr.sort(key=getKey)
    dots_val(otr)
    print(len(dots))
    print(' '.join(map(str, dots)))


def backpack(cw, w, keys):
    #########
    cw = {}
    count, weight = map(int, input().split())
    for i in range(count):
        c, w = map(int, input().split())
        cw[c / w] = [c, w]
    list_keys = list(cw.keys())
    list_keys.sort()
    print(backpack(cw, weight, list_keys))
    #########
    wt = 0
    money = 0.000
    for key in reversed(keys):
        if cw[key][1] <= w - wt:
            money = money + cw[key][0]
            wt = wt + cw[key][1]
        elif cw[key][1] > w - wt and w-wt != 0:
            money = money + (w-wt)*key
            return money
        else:
            return money
    return money


def numer():
    n = int(input())
    count = []
    summ = 0
    i = 1
    if n <= 2:
        count.append(n)
    else:
        while True:
            if summ + i <= n:
                count.append(i)
                summ += i
                i += 1
            else:
                if summ == n:
                    break
                count.remove(count[-1])
                last = n - sum(count)
                count.append(last)
                break
    print(len(count))
    print(' '.join(map(str, count)))
#############################
# Практика


def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]    # добавляем минус тк heapq реализует минкучу
    heapq.heapify(order) # делает кучу
    # order.sort(reverse=True) # Пары сравниваются лексикографически т.е. (v / w, w) до объема мы дойдем только если
    # ценность будет одинакова (первый вариант, без кучи)

    acc = 0
    while order and capacity:  # Третья реализация
        v_per_w, w = heapq.heappop(order)
        can_take = min(capacity, w)
        acc -= v_per_w * can_take
        capacity -= can_take
    # while order:  # Вторая реализация
    #     v_per_w, w = heapq.heappop(order)
    # if w < capacity:
    #     acc += -v_per_w * w
    #     capacity -= w
    # else:
    #     acc += -v_per_w * capacity
    #     break
    # for v_per_w, w in order:  # Первая реализация без кучи
    #     if w < capacity:
    #         acc += v_per_w * w
    #         capacity -= w
    #     else:
    #         acc += v_per_w * capacity
    #         break
    return acc


def backpack2():
    # line = input()  # строчка - строчка
    # реализует удобные возможности для консоли
    # Негативно сказываeтся на скорости
    next(sys.stdin)
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))


def test():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10**6)
        val_and_weights =[]
        for i in range(n):
            val_and_weights.append((randint(0, 2 * 10**6), randint(1, 2 * 10**6)))
        t = timed(fractional_knapsack, capacity, val_and_weights)
        assert t < 5


if __name__ == '__main__':
    backpack2()








