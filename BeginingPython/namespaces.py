class NameSpace:

    def __init__(self, n, p):
        self.parent = p
        self.name = n
        self.children = []

    def add(self, var):
        self.children.append(var)

    def get(self, var):
        for child in self.children:
            if child == var:
                print(self.name)
                return
        if self.parent is not None:
            self.parent.get(var)
        else:
            print("None")


def main():
    scopes = {}
    n = int(input())
    scopes["global"] = NameSpace("global", None)
    for i in range(n):
        cmd, namespace, arg = input().split()
        if cmd == "create":
            scopes[namespace] = NameSpace(namespace, scopes[arg])
        if cmd == "add":
            scopes[namespace].add(arg)
        if cmd == "get":
            scopes[namespace].get(arg)


if __name__ == '__main__':
    main()
