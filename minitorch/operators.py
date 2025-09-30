"""Collection of the core mathematical operators used throughout the code base."""

import math

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

def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def neg(a):
    return -a


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    return a if a > b else b


def is_close(a, b):
    return abs(a - b) < 0.01


def sigmoid(a):
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    else:
        return math.exp(a) / (1 + math.exp(a))


def relu(a):
    return max(0, a)


def log(a):
    return log(a)


def exp(a):
    return exp(a)


def inv(a):
    return 1 / a


def log_back(a, b):
    return b / a


def inv_back(a, b):
    return -b / (a ** 2)


def relu_back(a, b):
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

def map(iter, func):
    return [func(it) for it in iter]


def zipWith(iter1, iter2, func):
    res = list()
    for i in range(len(iter1)):
        res.append(func(iter1[i], iter2[i]))
    return res


def reduce(iter, func):
    if len(iter) == 1:
        return iter[0]
    res = iter[0]
    for i in range(1, len(iter)):
        res = func(res, iter[i])
    return res


def negList(l):
    return map(l, neg)


def addLists(l1, l2):
    return zipWith(l1, l2, add)


def sum(l):
    if len(l) == 0:
        return 0
    return reduce(l, add)


def prod(l):
    if len(l) == 0:
        return 1
    return reduce(l, mul)
