try:
    num = int(input("请输入整数："))
    res = 8 / num
except ZeroDivisionError:
    print("输入值不可为0")
except ValueError:
    print("输入值需为整数")
except Exception as result:
    print("未知错误")