class AvlTree:

    def __init__(self, n):
        self.last_sum = 0
        self.keys = []
        self.left_child = [-1 for _ in range(n + 1)]
        self.right_child = [-1 for _ in range(n + 1)]
        self.parent = [-1 for _ in range(n + 1)]

    def search(self, k, v=0):
        if self.keys[v] == k:
            return True, v
        if k < self.keys[v] and self.left_child[v] != -1:
            return self.search(k, self.left_child[v])
        if k > self.keys[v] and self.right_child[v] != -1:
            return self.search(k, self.right_child[v])
        return False, v

    def add(self, k):
        if len(self.keys) == 0:
            self.keys.append(k)
            return
        fl, v = self.search(k)
        if not fl:
            self.keys.append(k)
            index = len(self.keys) - 1
            self.parent[index] = v
            if k < self.keys[v]:
                self.left_child[v] = index
            if k > self.keys[v]:
                self.right_child[v] = index

    def splay(self, v):
        pass

    def remove(self, k):
        pass

    def in_order(self, v):
        if self.left_child[v] != -1:
            self.in_order(self.left_child[v])
        print(self.keys[v], end=' ')
        if self.right_child[v] != -1:
            self.in_order(self.right_child[v])


def main():
    n = int(input())
    tree = AvlTree(n)
    for i in range(n):
        tree.add(int(input()))

    tree.in_order(0)


if __name__ == '__main__':
    main()
