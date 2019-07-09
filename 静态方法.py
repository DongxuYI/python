class Dog:
    # 定义静态方法,不需要传入self,但是需要声明
    @staticmethod
    def run():
        print("跑跑")


wangcai = Dog()
wangcai.run()

# 静态方法可以通过实例调用,也可以通过类调用
# 如果一个方法既不调用类属性也不调用类方法,那么就可以将这个方法定义为静态方法
Dog.run()


