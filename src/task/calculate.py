import numpy as np

class Calculator:
    __init__ = None  # 防止实例化
    
    @staticmethod
    def _check_types(a, b, operation):
        """
        辅助检查函数：确保 a 和 b 符合运算条件。
        如果不符合，直接抛出 TypeError，终止计算。
        """
        # 判断是不是矩阵
        a_is_mat = isinstance(a, np.ndarray)
        b_is_mat = isinstance(b, np.ndarray)
        
        # 判断是不是数字（兼容 Python 和 NumPy 数字）
        a_is_num = isinstance(a, (int, float, np.integer, np.floating))
        b_is_num = isinstance(b, (int, float, np.integer, np.floating))
        
        a_is_int = isinstance(a, (int, np.integer))
        b_is_int = isinstance(b, (int, np.integer))
        
        if operation in ("加法","减法"):
        # 加减法计算条件：矩阵相加减,或数字相加减
            if not ((a_is_mat and b_is_mat) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")

        elif operation=="乘法":
        # 乘法计算条件：矩阵相乘，数字相乘，矩阵数乘
            if not ((a_is_mat and b_is_mat)or(a_is_num and b_is_num)or(a_is_num and b_is_mat)or(a_is_mat and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")
        
        elif operation in ("除法","取余","取整"):
        # 除法及取余取整计算条件：矩阵或数字除以(取余/取整)数字
            if not ((a_is_mat and b_is_num) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")
            
        elif operation == "幂":
        # 幂计算条件：矩阵的整数幂，数字的数字幂 
            if not ((a_is_mat and b_is_int) or (a_is_num and b_is_num)):
                raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")
            
        else:
            raise TypeError(f"{operation}不支持输入：{type(a).__name__} 和 {type(b).__name__}")
            
            
    
    @staticmethod
    def add(a,b):
        Calculator._check_types(a, b, "加法")
        return a+b
    
    @staticmethod
    def sub(a, b):
        Calculator._check_types(a, b, "减法")
        return a - b
    
    @staticmethod
    def mul(a, b):
        Calculator._check_types(a, b, "乘法")
        if isinstance(a,np.ndarray)and isinstance(b,np.ndarray):
            return a@b
        return a * b
    
    @staticmethod  
    def div(a, b):
        Calculator._check_types(a, b, "除法")
        return a / b
    
    @staticmethod
    def int_div(a, b):
        Calculator._check_types(a, b, "取余")
        return a // b
    
    @staticmethod
    def mod(a, b):
        Calculator._check_types(a, b, "取整")
        return a % b
    
    @staticmethod
    def pow(a, b):
        Calculator._check_types(a, b, "幂")
        if isinstance(a,np.ndarray) and isinstance(b,int):
                return np.linalg.matrix_power(a, b)
        return a ** b
    
if __name__ =="__main__":
    print("========== 我是直接运行模式 ==========")
    A = np.array([[1, 3],
                [2, 4]])
    B = np.array([[10, 20],
                [30, 40]])
    a=2
    b=3

    print(Calculator.pow(A,a))
    


