class dictionary_iter():
    def __init__(self, dict_input):
        self.dict_input = dict_input
        self.dict_keys = list(dict_input.keys())
        self.temp_index = 0

    def __iter__(self):
      return self

    def __next__(self):
        if self.temp_index < len(self.dict_keys):
            result = (self.dict_keys[self.temp_index], self.dict_input[self.dict_keys[self.temp_index]])
            self.temp_index += 1
            return result
        else:
            raise StopIteration()

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
