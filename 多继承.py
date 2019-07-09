class A:

    def test(self):
        print("A的test")

    def demo(self):
        print("A的demo")


class B:

    def test(self):
        print("B的test")

    def demo(self):
        print("B的demo")


class C(A, B):
    pass


# 方法重复,先入为主
c = C()
print(C.__mro__)
c.demo()
c.test()