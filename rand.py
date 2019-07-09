import random
item = ['one', 'two', 'three', 'four']
num1 = random.random()
num2 = random.randint(1, 5)  # 包括1和5
num3 = random.randrange(1, 5)  # 包括1不包括5
num4 = random.uniform(1, 5)  # 浮点数
num5 = random.choice(item)
'''
shuffle可以帮你把序列 item 中的元素随机打乱
random.sample(items, n) 方法可以从序列 items 中随机取出 n 个元素。

'''
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
