def test1():
    print('fun的test1')


def test2():
    print('test2_0')
    test1()
    print('test2_1')


def print_line(char, num, count):
    """

    :param char: 分割字符
    :param num: 每行多少个
    :param count: 多少行
    :return:
    """
    i = 0
    while i < count:
        print("%s" % char * num)
        i += 1


if __name__ == '__main__':
    test2()
    print_line('p', 50, 5)