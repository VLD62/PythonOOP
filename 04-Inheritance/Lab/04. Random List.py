import random

class RandomList(list):

    def get_random_element(self):
        return self.pop(random.randrange(len(self)))
