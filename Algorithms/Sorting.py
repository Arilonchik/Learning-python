from collections import deque


def merge(left, right, inversions_count):
    i = 0
    j = 0
    sum_m = []
    while len(left) != i or len(right) != j:
        if len(left) == i:
            sum_m += right[j:]
            break
        if len(right) == j:
            sum_m += left[i:]
            break
        if left[i] > right[j]:
            inversions_count += len(left) - i
            sum_m.append(right[j])
            j += 1
        else:
            sum_m.append(left[i])
            i += 1
    return sum_m, inversions_count


# just merging
def merge_sort(a):
    inversions = 0
    q = deque()
    for i in range(len(a)):
        q.append([a[i]])
    while len(q) > 1:
        merging, inversions = merge(q.popleft(), q.popleft(), inversions)
        q.append(merging)
    return q.popleft(), inversions

#####################################


counter = 0


def merge_sort_invers(a, l, r):
    if l < r:
        m = (l+r)//2
        msort = merge_inv(merge_sort_invers(a, l, m), merge_sort_invers(a, m+1, r))
    elif l == r:
        return [a[l]]
    return msort


def merge_inv(left, right):
    global counter
    i = 0
    j = 0
    msum = []
    while len(left) != i or len(right) != j:
        if len(left) == i:
            msum += right[j:]
            break
        if len(right) == j:
            msum += left[i:]
            break
        if left[i] > right[j]:
            counter += len(left) - i
            msum.append(right[j])
            j += 1
        else:
            msum.append(left[i])
            i += 1
    return msum


def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert n == len(a)
    # sorted_a, inversions = merge_sort(a)
    # print(inversions)
    # print(sorted_a)
    sorted_a = merge_sort_invers(a, 0, n-1)
    print(sorted_a)
    global counter
    print(counter)


######################################
# not mine


k = 0


def merge(a, b):
    tmp = []
    global k
    while a and b:
        if a[0] <= b[0]:
            tmp.append(a.pop(0))
        else:
            tmp.append(b.pop(0))
            k += len(a)
    tmp.extend(a or b)
    return tmp


def mergesort(lst):
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    return merge(mergesort(lst[: m]), mergesort(lst[m:]))


def main2():
    n = int(input())
    queue = [int(i) for i in input().split()]
    mergesort(queue)
    print(k)


if __name__ == '__main__':
    main()
