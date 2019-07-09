class Tools:
    count = 0

    def __init__(self):
        Tools.count += 1

    # @classmethod 定义类方法,通过cls访问类属性和类方法
    @classmethod
    def show_tool_count(cls):
        print(cls.count)


t1 = Tools()
t2 = Tools()

Tools.show_tool_count()