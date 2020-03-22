class reverse_iter():
    def __init__(self, nums_list):
        self.nums_list = nums_list
        self.list_len_ref = len(nums_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_len_ref >= 0:
            n = self.nums_list[self.list_len_ref]
            self.list_len_ref -= 1
            return n
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

