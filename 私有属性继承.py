class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("父类私有方法")

    def pub_fun(self):
        print("父类的公有方法")


class B(A):
    # 在子类中无法直接调用父类的私有属性和方法,但是可以访问父类的公有方法
    # 所以子类可以通过访问父类的公有方法间接访问父类的私有属性和方法
    # 子类只能调用自己的私有属性和方法
    def get_num(self):
        print(self.num1)
        self.pub_fun()


b = B()
b.get_num()
