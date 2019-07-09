
def input_pwd():
    pwd = input("请输入密码:")
    if len(pwd) >= 8:
        print(pwd)
    else:
        # 1.创建异常对象
        ex = Exception("密码长度不够")
        # 2.抛出异常
        raise ex


try:
    input_pwd()
except Exception as result:
    print("异常 %s" % result)
