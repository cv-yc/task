# tests/test_calculate.py
import numpy as np
import pytest
from task import calculate


# ========== 测试数据（固定值，保证可重复） ==========
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[10, 20], [30, 40]])


# ========== 加法 ==========
def test_add_num():
    assert calculate.Calculator.add(1, 2) == 3

def test_add_num_negative():
    assert calculate.Calculator.add(-5, 3) == -2

def test_add_mat():
    expected = np.array([[6, 8], [10, 12]])
    assert np.array_equal(calculate.Calculator.add(A, B), expected)

def test_add_type_error():
    with pytest.raises(TypeError):
        calculate.Calculator.add(A, 2)   # 矩阵 + 数字，应报错

def test_add_type_error_num_mat():
    with pytest.raises(TypeError):
        calculate.Calculator.add(2, A)   # 数字 + 矩阵，应报错


# ========== 减法 ==========
def test_sub_num():
    assert calculate.Calculator.sub(5, 3) == 2

def test_sub_mat():
    expected = np.array([[-4, -4], [-4, -4]])
    assert np.array_equal(calculate.Calculator.sub(A, B), expected)

def test_sub_type_error():
    with pytest.raises(TypeError):
        calculate.Calculator.sub(A, 2)


# ========== 乘法 ==========
def test_mul_num():
    assert calculate.Calculator.mul(2, 3) == 6

def test_mul_mat_mat():
    """矩阵 × 矩阵 → 矩阵乘法"""
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(calculate.Calculator.mul(A, B), expected)

def test_mul_mat_num():
    """矩阵 × 数字 → 数乘"""
    expected = np.array([[2, 4], [6, 8]])
    assert np.array_equal(calculate.Calculator.mul(A, 2), expected)

def test_mul_num_mat():
    """数字 × 矩阵 → 数乘"""
    expected = np.array([[2, 4], [6, 8]])
    assert np.array_equal(calculate.Calculator.mul(2, A), expected)

def test_mul_type_error():
    with pytest.raises(TypeError):
        calculate.Calculator.mul(A, "hello")   # 矩阵 × 字符串，应报错


# ========== 除法 ==========
def test_div_num():
    assert calculate.Calculator.div(10, 2) == 5

def test_div_mat_num():
    """矩阵 ÷ 数字"""
    expected = np.array([[0.5, 1.0], [1.5, 2.0]])
    assert np.array_equal(calculate.Calculator.div(A, 2), expected)

def test_div_type_error_num_mat():
    with pytest.raises(TypeError):
        calculate.Calculator.div(2, A)   # 数字 ÷ 矩阵，应报错

def test_div_type_error_mat_mat():
    with pytest.raises(TypeError):
        calculate.Calculator.div(A, B)   # 矩阵 ÷ 矩阵，应报错


# ========== 取整除法 ==========
def test_int_div_num():
    assert calculate.Calculator.int_div(10, 3) == 3

def test_int_div_mat_num():
    expected = np.array([[0, 1], [1, 2]])
    assert np.array_equal(calculate.Calculator.int_div(A, 2), expected)

def test_int_div_type_error():
    with pytest.raises(TypeError):
        calculate.Calculator.int_div(A, B)


# ========== 取余 ==========
def test_mod_num():
    assert calculate.Calculator.mod(10, 3) == 1

def test_mod_mat_num():
    expected = np.array([[1, 0], [1, 0]])
    assert np.array_equal(calculate.Calculator.mod(A, 2), expected)

def test_mod_type_error():
    with pytest.raises(TypeError):
        calculate.Calculator.mod(A, B)


# ========== 幂运算 ==========
def test_pow_num():
    assert calculate.Calculator.pow(2, 3) == 8

def test_pow_mat_int():
    """矩阵的整数次幂 → A @ A"""
    expected = A @ A
    assert np.array_equal(calculate.Calculator.pow(A, 2), expected)

def test_pow_mat_zero():
    """矩阵的 0 次方 → 单位矩阵"""
    expected = np.eye(2)
    assert np.array_equal(calculate.Calculator.pow(A, 0), expected)

def test_pow_type_error_mat_float():
    with pytest.raises(TypeError):
        calculate.Calculator.pow(A, 0.5)   # 矩阵 ** 小数，应报错

def test_pow_type_error_num_mat():
    with pytest.raises(TypeError):
        calculate.Calculator.pow(2, A)     # 数字 ** 矩阵，应报错
