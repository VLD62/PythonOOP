class take_skip():
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.temp_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp_num <= (self.step * self.count) - self.step:
            n = self.temp_num
            self.temp_num += self.step
            return n
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
