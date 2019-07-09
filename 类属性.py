class Tools:
    # 定义类属性,记录实例化的次数
    # 类属性是用来记录类的相关特征
    count = 0

    def __init__(self):
        Tools.count += 1


t1 = Tools()
t2 = Tools()
print(Tools.count)

# python的属性获取机制
# 向上查找,先在实例里寻找,如果没有就向上查找

t2.count = 5
print(t2.count)