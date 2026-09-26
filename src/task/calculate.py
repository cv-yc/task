import numpy as np


class Calculator:
    """
    计算器类，支持数字与矩阵的加、减、乘、除、取整、取余、幂运算。

    注意：所有方法都是静态方法，不需要创建实例，直接用类名调用即可。
    例如：Calculator.add(1, 2)
    """

    # 禁止实例化：把 __init__ 设为 None，这样 Calculator() 会报错
    __init__ = None

    @staticmethod
    def _check_types(a, b, operation):
        """
        辅助检查函数：确保 a 和 b 符合指定运算的类型要求。

        参数：
            a, b      : 参与运算的两个操作数
            operation : 运算名称（"加法"、"减法"、"乘法"、"除法"、"取余"、"取整"、"幂"）

        如果类型不匹配，直接抛出 TypeError，终止计算。
        """
        # 判断 a、b 是否都是矩阵（numpy 数组）
        a_is_mat = isinstance(a, np.ndarray)
        b_is_mat = isinstance(b, np.ndarray)

        # 判断 a、b 是否都是数字（兼容 Python 和 NumPy 的数字类型）
        a_is_num = isinstance(a, (int, float, np.integer, np.floating))
        b_is_num = isinstance(b, (int, float, np.integer, np.floating))

        # 判断 a、b 是否都是整数（用于矩阵幂运算的限制）
        a_is_int = isinstance(a, (int, np.integer))
        b_is_int = isinstance(b, (int, np.integer))

        if operation in ("加法", "减法"):
            # 加减法：只允许「矩阵 + 矩阵」或「数字 + 数字」
            if not ((a_is_mat and b_is_mat) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

        elif operation == "乘法":
            # 乘法：允许「矩阵 × 矩阵」「数字 × 数字」「矩阵 × 数字」「数字 × 矩阵」
            if not ((a_is_mat and b_is_mat) or (a_is_num and b_is_num)
                    or (a_is_num and b_is_mat) or (a_is_mat and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

        elif operation in ("除法", "取余", "取整"):
            # 除法、取余、取整：只允许「矩阵 / 数字」或「数字 / 数字」
            if not ((a_is_mat and b_is_num) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

        elif operation == "幂":
            # 幂运算：只允许「矩阵 ** 整数」或「数字 ** 数字」
            if not ((a_is_mat and b_is_int) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

        else:
            # 未知运算：直接报错
            raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

    @staticmethod
    def add(a, b):
        """加法：矩阵 + 矩阵，或数字 + 数字。"""
        Calculator._check_types(a, b, "加法")
        return a + b

    @staticmethod
    def sub(a, b):
        """减法：矩阵 - 矩阵，或数字 - 数字。"""
        Calculator._check_types(a, b, "减法")
        return a - b

    @staticmethod
    def mul(a, b):
        """
        乘法：
        - 矩阵 × 矩阵 → 矩阵乘法（@）
        - 其他组合   → 普通乘法（*），即数乘
        """
        Calculator._check_types(a, b, "乘法")
        if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
            return a @ b
        return a * b

    @staticmethod
    def div(a, b):
        """除法：矩阵 / 数字，或数字 / 数字。"""
        Calculator._check_types(a, b, "除法")
        return a / b

    @staticmethod
    def int_div(a, b):
        """取整除法：矩阵 // 数字，或数字 // 数字。"""
        Calculator._check_types(a, b, "取余")
        return a // b

    @staticmethod
    def mod(a, b):
        """取余：矩阵 % 数字，或数字 % 数字。"""
        Calculator._check_types(a, b, "取整")
        return a % b

    @staticmethod
    def pow(a, b):
        """
        幂运算：
        - 矩阵 ** 整数 → 矩阵的整数次幂（用 np.linalg.matrix_power）
        - 其他组合     → 普通幂运算（**）
        """
        Calculator._check_types(a, b, "幂")
        if isinstance(a, np.ndarray) and isinstance(b, int):
            return np.linalg.matrix_power(a, b)
        return a ** b
    


