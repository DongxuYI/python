from distutils.core import setup

setup(name="YI",  # 包名
      version=1.0,  # 版本
      description="测试发布",  # 描述
      long_description="还是测试发布",  # 长描述
      author="YI",  # 作者
      author_email="1635599439@qq.com",  # 邮箱
      url="www.baidu.com",  # 主页
      py_modules=["package_message.send_message", "package_message.receive_message"])