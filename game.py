class Game:
    max_score = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "用户 %s 最高分为 %d" % (self.name, Game.max_score)

    @staticmethod
    def help():
        print("help")

    @classmethod
    def show_max_score(cls):
        print("游戏最高分为 %d" % cls.max_score)

    def start(self, current_score):
        if current_score >= Game.max_score:
            print("%s 破纪录了,最高分为 %d" % (self.name, current_score))
            Game.max_score = current_score
        else:
            print("%s 游戏结束,最高分为 %d" % (self.name, Game.max_score))


p1 = Game("玩家1")
p1.start(20)
print(p1)