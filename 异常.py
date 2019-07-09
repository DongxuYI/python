def get():
    try:
        num = int(input("请输入整数:"))
        result = 8 / num
        print(result)
    except ZeroDivisionError:
        print("输入不可为0")
    except ValueError:
        print("请输入整数")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("没有异常就会执行到这里")
    finally:
        print("无论是否有异常都会执行到这里")


# 可以利用异常的传递性在主程序捕获
get()