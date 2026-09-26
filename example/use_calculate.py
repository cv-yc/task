# 从 task 包里导入 calculate 模块
from task import calculate

# 加法：1 + 2 = 3
print(calculate.Calculator.add(1, 2))     # 3

# 减法：5 - 3 = 2
print(calculate.Calculator.sub(5, 3))     # 2

# 乘法：2 × 3 = 6
print(calculate.Calculator.mul(2, 3))     # 6

# 幂运算：2^3 = 8
print(calculate.Calculator.pow(2, 3))     # 8