# import  cardTools
info = [
    {
        'name': '44',
        'tel': '44',
        'qq': '44'
    }
]


def init():
    print('*' * 50)
    print('1.新建')
    print('2.全部')
    print('3.查询')
    print('\t')
    print('0.退出')
    print('*' * 50)
    while True:
        num = input("请输入编号:")
        if num == '0':
            break
        elif num == '1':
            print('新建用户')
            create()
        elif num == '2':
            print('全部用户')
            total()
        elif num == '3':
            print('查询用户')
            query_str = input("请输入查询用户名:")
            query(query_str)
        else:
            print('输入错误,请重新输入')


def create():
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    qq = input("请输入qq:")
    obj = {
        'name': name,
        'tel': tel,
        'qq': qq
    }
    info.append(obj)
    print(info)
    init()


def total():
    print(info)
    init()


def query(query_str):
    for item in info:
        if item['name'] == query_str:
            print(item)
            break
    else:
        print('查询无结果')
        init()


init()