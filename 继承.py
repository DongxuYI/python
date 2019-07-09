class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):

    def __init__(self, color):
        # super().__init__(self, name, age)
        self.color = color

    # 方法的重写,覆盖父类的方法
    def run(self):
        print("子类的run")

    # 扩展父类方法,在父类的基础上添加
    def eat(self):
        super().eat()
        print("新吃法")

    def bark(self):
        print("brak")


gou = Dog("二哈")
# print(gou.name)
gou.eat()