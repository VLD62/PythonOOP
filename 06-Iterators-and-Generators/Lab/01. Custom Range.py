class custom_range():
    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_num <= self.end_num:
            n = self.start_num
            self.start_num += 1
            return n
        else:
            raise StopIteration()



one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
