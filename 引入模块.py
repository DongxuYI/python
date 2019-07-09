# 引入模块时,所有没有缩进的代码都会被执行
# __name__属性,只在模块内执行,不被其他模块引用
from functionMap import test1
import kw

test1()
kw.test1()