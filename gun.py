class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet = 0

    def __str__(self):
        return "%s 还有 %s 颗子弹" % (self.model, self.bullet)

    def add_bullet(self, count):
        self.bullet = count

    def shoot(self):
        if self.bullet <= 0:
            print("%s 没有子弹了" % self.model)
            return
        else:
            print("biu～～～")
            self.bullet -= 1


gun = Gun("AK47")
# gun.add_bullet(200)
# gun.shoot()
# print(gun)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return "%s 枪 % s" % (self.name, self.gun)

    def fire(self):
        if self.gun is None:
            print("%s 没有枪" % self.name)
            return
        if self.gun.bullet <= 0:
            print("没有子弹,自动填充")
            self.gun.add_bullet(100)
        self.gun.shoot()
        print("%s 冲锋" % self.name)


xu = Soldier("许三多")
xu.gun = gun
xu.fire()
print(xu)

"""
python身份运算符is,is not
用来判断两个对象的地址是否相同
== 值判断两个对象的值是否相等
id()
a = [1, 2, 3]
b = [1, 2]
id(a)和id(b)肯定不同
b.append(3)
这个时候(a == b) = True
"""