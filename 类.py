"""
创建对象的过程:
1.分配空间
2.设置初始值,初始化方法__init__,在创建对象时会自动调用init方法,
    可以在创建对象的同时就设置对象的属性,在init方法内添加
    同时也可以传递参数

"""


class Cat:
    def __init__(self, name):
        self.name = name

    # 当对象被销毁前会自动调用del方法

    def __del__(self):
        print("被销毁了")

    def __str__(self):  # 必须返回一个字符串
        return "这是一只猫[%s]" % self.name

    def eat(self):
        print("%s 在吃" % self.name)


cat1 = Cat('Jack')
cat1.eat()
print(cat1)

# cat1是一个全局变量,会等全部执行完再被销毁
print("-" * 50)

del cat1  # 销毁对象
print("-" * 50)

