import bisect
import sys


def main():
    n, m = map(int, input().split())
    lines = []
    for i in range(n):
        a = list(map(int, input().split()))
        lines.append(a)
    dots = list(map(int,input().split()))
    # reader = (list(map(int, line.split())) for line in sys.stdin)
    # n, m = next(reader)
    # lines = list(reader)
    # dots = lines.pop(-1)

    begins = list(quick_sort(lines, 0, len(lines)-1, 0))
    ends = list(quick_sort(lines, 0, len(lines)-1, 1))
    only_b = []
    only_e = []
    for i in range(len(begins)):
        only_b.append(begins[i][0])
        only_e.append(ends[i][1])
    ans = ''
    cb_dot = {}
    for dot in dots:
        cb_dot[dot] = bisect.bisect(only_b, dot)
        ind = bisect.bisect(only_e, dot)
        ind_l = bisect.bisect_left(only_e, dot)
        ind = ind - (ind-ind_l)
        cb_dot[dot] = cb_dot[dot] - ind
        ans += str(cb_dot[dot]) + ' '
    print(ans)


def quick_sort(lines, l, r, key):
    # if l >= r:
    #     return lines
    # end, begin = partition(lines, l, r, key)
    # quick_sort(lines, l, begin - 1, key)
    # quick_sort(lines, end + 1, r, key)

    while l < r:
        end, begin = partition(lines, l, r, key)
        if len(lines[l:begin-1]) > len(lines[end+1: r]):
            quick_sort(lines, end + 1, r, key)
            r = begin - 1
        else:
            quick_sort(lines, l, begin - 1, key)
            l = end + 1
    return lines


def partition(lines, l, r, key):
    mid = (l+r)//2
    lines[l], lines[mid] = lines[mid], lines[l]
    bearning_x = lines[l][key]
    index = l
    equals_index = l
    count = 0
    for i in range(l + 1, r + 1):
        if lines[i][key] < bearning_x:
            index += 1
            lines[index], lines[i] = lines[i], lines[index]
        if lines[i][key] == bearning_x:
            equals_index += 1
            index += 1
            lines[index], lines[i] = lines[i], lines[index]
            lines[equals_index], lines[index] = lines[index], lines[equals_index]
    if equals_index == l:
        lines[l], lines[index] = lines[index], lines[l]
    else:
        in_old = index
        count -= 1
        for i in range(l, equals_index + 1):
            lines[i], lines[in_old] = lines[in_old], lines[i]
            in_old -= 1
            count += 1
    return index, index - count


if __name__ == '__main__':
    main()
