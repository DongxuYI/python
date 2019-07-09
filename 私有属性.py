class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __str__(self):
        return "%s 的年龄是 %d" % (self.name, self.__age)

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


women = Women("小美")

# 私有属性(方法)外接不能访问
# print(women.__age)

# 在对象的方法内部可以调用私有属性(方法)
women.secret()
# python并没有真正意义上的私有,可以通过 对象._类名__属性(方法) 访问
print(women._Women__age)
