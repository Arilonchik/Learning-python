class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError(str(x) + " is not positive")
###########################


class NonPositiveError(ArithmeticError):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        super().append(x)


if __name__ == '__main__':
    a = PositiveList()
    #a.append(-5)
    a.append(5)