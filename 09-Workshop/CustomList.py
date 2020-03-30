class CustomList:
    def __init__(self, *args):
        self.listche = [x for x in args]

    def append(self, element):
        self.listche.insert(len(self.listche), element)
        return self.listche

    def remove(self, index):
        del self.listche[index]
        return self.listche

    def get(self, index):
        return self.listche[index]

    def extend(self, iterable):
        self.listche += iterable
        return self.listche

    def insert(self, index, element):
        self.listche.insert(index, element)
        return self.listche

    def pop(self):
        value = self.listche[-1]
        del self.listche[-1]
        return value

    def clear(self):
        self.listche = []

    def index(self, value):
        for i, j in enumerate(self.listche):
            if j == value:
                return i

    def count(self, value):
        counter = 0
        for i, j in enumerate(self.listche):
            if j == value:
                counter += 1
        return counter

    def reverse(self):
        return self.listche[::-1]

    def copy(self):
        copy_list = self.listche.copy()
        return copy_list

    def size(self):
        return len(self.listche)

    def add_first(self, value):
        self.insert(0,value)

    def dictionize(self):
        temp_dict = {}
        for i, j in enumerate(self.listche):
            if i % 2 == 0:
                try:
                    temp_dict[j] = self.listche[i+1]
                except:
                    temp_dict[j] = " "
        return temp_dict

    def move(self, amount):
        temp_list = self.listche[:amount]
        self.listche = self.listche[amount:]
        self.listche = self.extend(temp_list)
        return self.listche

    def sum(self):
        total_sum = 0
        for element in self.listche:
            try :
                total_sum += int(element)
            except:
                total_sum += len(element)
        return total_sum

    def overbound(self):
        temp_list = []
        for element in self.listche:
            try :
                value = int(element)
            except:
                value = len(element)
            temp_list.append(value)
        biggest = temp_list[0]
        biggest_idx = 0
        for idx, element in enumerate(temp_list):
            if element > biggest:
                biggest = element
                biggest_idx = idx
        return biggest_idx

    def underbound(self): 
        temp_list = []
        for element in self.listche:
            try :
                value = int(element)
            except:
                value = len(element)
            temp_list.append(value)
        smallest = temp_list[0]
        smallest_idx = 0
        for idx, element in enumerate(temp_list):
            if element < smallest:
                smallest = element
                smallest_idx = idx
        return smallest_idx

    def __repr__(self):
        self.listche = [str(x) for x in self.listche]
        return f'''['{"', '".join(self.listche)}']'''

