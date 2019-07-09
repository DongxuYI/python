# 创建实例时会先调用内置方法__new__分配地址
# __new__的作用有两个,在内存中为对象分配空间,返回对象的引用


# 在创建实例时,会做两件事,利用__new__为对象分配空间,利用__init__初始化对象

class Player:
    # 只分配一次空间
    instance = None

    # 只执行一次初始化
    init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
        # print("create")
        # # 1.super().__new__(cls) 分配空间
        # # 2.return 返回对象
        # return super().__new__(cls)

    def __init__(self):
        if Player.init_flag:
            print("start")
            Player.init_flag = False


player = Player()
print(player)

pl = Player()
print(pl)