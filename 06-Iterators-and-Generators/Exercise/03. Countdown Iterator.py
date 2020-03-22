class countdown_iterator():
    def __init__(self, num):
        self.num = num


    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= 0: 
            result = self.num
            self.num -= 1
            return result
        else:
            raise StopIteration()

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
