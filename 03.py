class Human (object):
    def __init__(self, name):
        self.taisheng = True
        self.name = name

    def walk(self):
        print(self.name + ' is walking')

    def handle(self):
        return self.name

    def change(self, name):
        self.name = name
# human_a = Human('YI')
# human_a.walk()
# print(human_a.handle())
# human_a.change('ER')
# print(human_a.handle())
# print(human_a.name)


class Man(Human):
    def __init__(self, name, married):
        Human.__init__(self, name)
        self.name = name
        self.married = married


man_a = Man('YI', False)
man_a.walk()
print(man_a.taisheng)