class LoggableList(list, Loggable):
    def append(self, var):
        super(LoggableList, self).append(var)
        super(LoggableList, self).log(var)
##############################


class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)