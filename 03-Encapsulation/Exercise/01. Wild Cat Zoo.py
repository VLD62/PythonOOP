class Lion:
    def __init__(self, name: str, gender: str , age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Tiger:
    def __init__(self, name: str, gender: str , age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Cheetah:
    def __init__(self, name: str, gender: str , age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Keeper:
    def __init__(self, name: str, age: int , salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Caretaker:
    def __init__(self, name: str, age: int , salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Vet:
    def __init__(self, name: str, age: int , salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Zoo:
    def  __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if isinstance(animal, Lion) or isinstance(animal, Tiger) or isinstance(animal, Cheetah):
            if self.__budget >= price and self.__animal_capacity > 0:
                self.__budget -= price
                self.__animal_capacity -= 1
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            elif self.__animal_capacity > 0:
                return f"Not enough budget"
            else:
                return f"Not enough space for animal"

    def hire_worker(self, worker):
        if isinstance(worker, Keeper) or isinstance(worker, Caretaker) or isinstance(worker, Vet):
            if self.__workers_capacity > 0:
                self.workers.append(worker)
                return f"{worker.name} the {worker.__class__.__name__} hired successfully"
            else:
                return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = 0
        for worker in self.workers:
            salary_sum += worker.salary
        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_sum = 0
        for animal in self.animals:
            tend_sum += animal.get_needs()
        if self.__budget >= tend_sum:
            self.__budget -= tend_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        amount_of_lions = 0
        amount_of_tigers = 0
        amount_of_cheetahs = 0
        result = f"You have {len(self.animals)} animals\n"
        for animal in self.animals:
            if isinstance(animal, Lion):
                amount_of_lions += 1
            elif isinstance(animal, Tiger):
                amount_of_tigers += 1
            elif isinstance(animal, Cheetah):
                amount_of_cheetahs += 1
        if amount_of_lions > 0:
            result += f"----- {amount_of_lions} Lions:\n"
            for animal in self.animals:
                if isinstance(animal, Lion):
                    result += f"{animal}\n"
        if amount_of_tigers > 0:
            result += f"----- {amount_of_tigers} Tigers:\n"
            for animal in self.animals:
                if isinstance(animal, Tiger):
                    result += f"{animal}\n"
        if amount_of_cheetahs > 0:
            result += f"----- {amount_of_cheetahs} Cheetahs:\n"
            for animal in self.animals:
                if isinstance(animal, Cheetah):
                    result += f"{animal}\n"
        return result

    def workers_status(self):
        amount_of_keepers = 0
        amount_of_caretakers = 0
        amount_of_vetes = 0
        result = f"You have {len(self.workers)} workers\n"
        for worker in self.workers:
            if isinstance(worker, Keeper):
                amount_of_keepers += 1
            elif isinstance(worker, Caretaker):
                amount_of_caretakers += 1
            elif isinstance(worker, Vet):
                amount_of_vetes += 1
        if amount_of_keepers > 0:
            result += f"----- {amount_of_keepers} Keepers:\n"
            for worker in self.workers:
                if isinstance(worker, Keeper):
                    result += f"{worker}\n"
        if amount_of_caretakers > 0:
            result += f"----- {amount_of_caretakers} Caretakers:\n"
            for worker in self.workers:
                if isinstance(worker, Caretaker):
                    result += f"{worker}\n"
        if amount_of_vetes > 0:
            result += f"----- {amount_of_vetes} Vets:\n"
            for worker in self.workers:
                if isinstance(worker, Vet):
                    result += f"{worker}\n"
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
