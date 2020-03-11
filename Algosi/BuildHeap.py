def main():
    n = int(input())
    heap = list(map(int, input().split()))
    changes = []
    for i in range((len(heap) // 2)-1, -1, -1):
        sift_down(i, heap, changes)
    print(len(changes))
    for change in changes:
        print(*change)


def sift_down(i, heap, changes):
    changing_index = i
    l = 2 * i + 1
    if l <= len(heap)-1 and heap[l] < heap[changing_index]:
        changing_index = l
    r = 2 * i + 2
    if r <= len(heap)-1 and heap[r] < heap[changing_index]:
        changing_index = r
    if changing_index != i:
        heap[i], heap[changing_index] = heap[changing_index], heap[i]
        changes.append((i, changing_index))
        sift_down(changing_index, heap, changes)


if __name__ == '__main__':
    main()
