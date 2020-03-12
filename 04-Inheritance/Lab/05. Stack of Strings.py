class Stack:

    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.insert(0, item)

    def pop(self):
        if self.__data:
            return self.__data.pop(0)

    def peek(self):
        if self.__data:
            return self.__data[-1]

    def is_empty(self):
        result = True
        if len(self.__data) > 0:
            result = False
        return result

    def __repr__(self):
        data = [str(x) for x in self.__data]
        return f"[{', '.join(data)}]"
