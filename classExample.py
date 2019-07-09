# import keyword
# print(keyword.kwlist)


class Animal(object):

    @classmethod
    def eat(cls):
        pass

    def run(self):
        print('run')


class Human(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age


human1 = Human('YI', 18)
human2 = Human('YI', 18)
human3 = Human('YI', 18)
print(human1.age)
print(Human.sum1)