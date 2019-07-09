def get_sum(num):
    if num == 1:
        return 1
    res = num * get_sum(num-1)
    return res


result = get_sum(6)
print(result)


def aa(start, end, step):
    """

    :param start: 开始值
    :param end: 结束值
    :param step: 步长(如果开始值>结束值,步长自动为负数,开始值<结束值,步长为正)
    :return:
    """
    if start > end:
        step = -abs(step)
        if start+step <= end:
            return start+step
    else:
        step = abs(step)
        if start+step >= end:
            return start+step

    res = start + aa(start+step, end, step)
    return res


aaa = aa(10, 20, 2)
print(aaa)