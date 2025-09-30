"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(a: float, b: float) -> float:
    return a * b


def id(a: float) -> float:
    return a


def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def lt(a: float, b: float) -> float:
    return a < b


def eq(a: float, b: float) -> float:
    return a == b


def max(a: float, b: float) -> float:
    return a if a > b else b


def is_close(a: float, b: float) -> float:
    return abs(a - b) < 0.01


def sigmoid(a: float) -> float:
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    else:
        return math.exp(a) / (1 + math.exp(a))


def relu(a: float) -> float:
    return max(0, a)


def log(a: float) -> float:
    return math.log(a)


def exp(a: float) -> float:
    return math.exp(a)


def inv(a: float) -> float:
    return 1 / a


def log_back(a: float, b: float) -> float:
    return b / a


def inv_back(a: float, b: float) -> float:
    return -b / (a ** 2)


def relu_back(a: float, b: float) -> float:
    return b * (a > 0)


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(iter: Iterable[float], func: Callable[[float], float]) -> Iterable[float]:
    return [func(it) for it in iter]


def zipWith(iter1: Iterable[float], iter2: Iterable, func: Callable[[float], float]) -> Iterable[float]:
    res = list()
    for i in range(len(iter1)):
        res.append(func(iter1[i], iter2[i]))
    return res


def reduce(iter: Iterable[float], func: Callable[[float], float]) -> Iterable[float]:
    if len(iter) == 1:
        return iter[0]
    res = iter[0]
    for i in range(1, len(iter)):
        res = func(res, iter[i])
    return res


def negList(l: Iterable[float]) -> Iterable[float]:
    return map(l, neg)


def addLists(l1: Iterable[float], l2: Iterable[float]) -> Iterable[float]:
    return zipWith(l1, l2, add)


def sum(l: Iterable[float]) -> Iterable[float]:
    if len(l) == 0:
        return 0
    return reduce(l, add)


def prod(l: Iterable[float]) -> Iterable[float]:
    if len(l) == 0:
        return 1
    return reduce(l, mul)
