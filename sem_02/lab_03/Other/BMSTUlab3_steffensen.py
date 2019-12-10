from math import *


def f(x):
    return x ** 3 - 2 * x ** 2 + 1


def str_f():
    return "sin(x)"


def steffensen_root_finding(left_verge, right_verge, eps, max_iters, x_curr):
    current_iters = 0

    if f(x_curr) == 0:
        return x_curr, 0, 0

    x_next = x_curr - f(x_curr) ** 2 / (f(x_curr + f(x_curr)) - f(x_curr))

    while abs(x_curr - x_next) > eps:
        current_iters += 1

        if not (left_verge <= x_next <= right_verge):
            return None, current_iters, 2

        if current_iters >= max_iters:
            return x_next, current_iters, 1

        x_curr = x_next
        div_part = (f(x_curr + f(x_curr)) - f(x_curr))

        if div_part == 0:
            return x_next, current_iters, 0

        x_next = x_curr - f(x_curr) ** 2 / div_part

    if not (left_verge <= x_next <= right_verge):
        return None, current_iters, 2

    return x_next, current_iters, 0
