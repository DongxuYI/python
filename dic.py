obj = {
    'name': 'YI',
    'age': 23
}
obj1 = {
    'sex': 'male'
}

# for key in obj:
#     print(key)

# print(obj.keys())
# print(obj.items())
# print(obj.get('age'))

# 键值对数量
len(obj)

# 合并字典,如果有相同键,会被覆盖
obj.update(obj1)

print(obj)