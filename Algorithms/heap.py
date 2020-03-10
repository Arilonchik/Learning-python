import sys


class MaxHeap:
    def __init__(self):
        self.heap = {}

    def siftup(self, n, parent):
        if parent == 0:
            return False, parent
        if self.heap[parent] < self.heap[n]:
            self.heap[parent], self.heap[n] = self.heap[n], self.heap[parent]
        else:
            return False, parent
        return True, parent

    def insert(self, p):
        self.heap[len(self.heap)+1] = p
        n = len(self.heap)
        f = True
        parent = len(self.heap) // 2
        while f:
            f, n = self.siftup(n, parent)
            parent = n // 2

    def siftdown(self, n):
        child1 = 2*n
        child2 = 2*n+1
        if child1 in self.heap and child2 in self.heap:
            d = {child1: self.heap[child1], child2: self.heap[child2]}
            maxel = max(d, key=lambda unit: d[unit])
            if self.heap[n] < self.heap[maxel]:
                self.heap[maxel], self.heap[n] = self.heap[n], self.heap[maxel]
                self.siftdown(maxel)
        if child1 in self.heap and (child2 not in self.heap):
            if self.heap[n] < self.heap[child1]:
                self.heap[child1], self.heap[n] = self.heap[n], self.heap[child1]
        if child2 in self.heap and (child1 not in self.heap):
            if self.heap[n] < self.heap[child2]:
                self.heap[child2], self.heap[n] = self.heap[n], self.heap[child2]

    def extractmax(self):
        self.heap[1], self.heap[len(self.heap)] = self.heap[len(self.heap)], self.heap[1]
        maximum = self.heap.pop(len(self.heap))
        self.siftdown(1)
        return maximum


if __name__ == '__main__':
    hp = MaxHeap()
    count = int(input())
    for i in range(count):
        command = sys.stdin.readline()
        command = command.split(' ')
        if len(command) > 1:
            hp.insert(int(command[1]))
        else:
            print(hp.extractmax())
