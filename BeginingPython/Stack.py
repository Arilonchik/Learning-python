class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())


if __name__ == '__main__':
    a = ExtendedStack()
    a.extend([i for i in range(15)])
    print(a)
    a.sum()
    print(a)
    a.mul()
    print(a)
    a.div()
    print(a)
    a.sub()
    print(a)
