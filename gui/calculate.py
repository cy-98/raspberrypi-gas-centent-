from gui.validate import validate
from gui.hooks.useStore import useStore
from err import ErrorArrLength
from util import last
from functools import reduce
from gui.const import (
    AREA_LABEL,
    DEFAULT_ATOMSPHERIC,
    DEFAULT_DENSITY,
    DEFAULT_GRAVITY,
    FETCH_V,
    FETCH_P,
    DENSITY_LABEL,
    ATMOSPHERIC_LABEL,
    GRAVITY_LABEL,
)


def calcByPressure(G, currentP, ρ, g):
    # currentP 当前大气压强
    # ρ 当前水密度
    # g 当地重力加速度
    # G 传感器所测得重力数值
    # V = P' / P × G / ρ × g
    # 体积 = 压强换算 （ 密度质量计算）
    # 当地压强/ 标准大气压强 1.013×10e5

    P = DEFAULT_ATOMSPHERIC

    return currentP / P * G / ρ * g


def calcByRatio(x, y, S):
    # x为时间序列
    # y为传感器数值
    # 对y积分得出累计结果
    # S: 管道横截面积

    # res: 结果变量
    # index: y坐标
    # pre: 前一位x的数值
    res = 0
    index = 0
    pre = 0

    for cur in x:
        Y = y[index]
        dx = cur - pre
        res += dx * Y

        index += 1
        pre = cur

    return res * S


def calculate():
    result = None
    store, _ = useStore()
    curType = store['type']
    values = store['ydata']

    if len(values) < 0:
        ErrorArrLength('ydata from sensor')

    if curType == FETCH_P:
        p = store[ATMOSPHERIC_LABEL]  # 大气压强参数
        ρ = store[DENSITY_LABEL]  # 水密度参数
        g = store[GRAVITY_LABEL]  # 重力加速度参数
        G = last(values)
        result = calcByPressure(G, p, ρ, g)
    else:
        S = store[AREA_LABEL]
        result = calcByRatio(store['xdata'], values, S)

    return result
