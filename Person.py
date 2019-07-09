class Person:  # 类似js构造函数
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 我的体重是 %.2f KG" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("跑个步")

    def eat(self):
        self.weight += 1
        print("吃点东西")


xiaoming = Person('小明', 75.0)
xiaomei = Person('小美', 45.0)

xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)

xiaomei.run()
xiaomei.eat()
xiaomei.run()
xiaomei.run()
print(xiaomei)