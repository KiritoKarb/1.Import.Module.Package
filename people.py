class Person:
    def __init__(self, name):
        self.name = name
        self.salary = []

man = Person('Adriej')
for i in range(1, 20, 2):
    man.salary.append(10)
