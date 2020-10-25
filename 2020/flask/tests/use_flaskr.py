#_*_coding:utf-8_*_
import sys

# 动态添加test_package文件夹的路径，为了能让此文件夹下的
# 自定义包成功的导入
# 要根据你自己的实际包的模块来决定路径。
sys.path.append('/home/jax/work/dev/record/2020/flask/flaskr')

# 打印所有python解释器可以搜索到的所有路径
print(sys.path)

# 导入自定义包
from flaskr import *

# 输出lucky_package中test函数的结果：
result = test()
print(result)