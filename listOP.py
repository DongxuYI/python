name_list = ['111', '222', '333', '444', '666', '555', '666', '777', '888']
name_list1 = ['555', '666', '777', '888']
# name_list.insert(3, '222')
# name_list.extend(name_list1)
# print(name_list)

list_len = len(name_list)
i = 0
while i < list_len:
    num = name_list.count(name_list[i])
    print("%s 出现了 %d 次" % (name_list[i], num))
    i += 1