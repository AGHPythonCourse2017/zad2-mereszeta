import math


class FunctionProvider:
    @staticmethod
    def o_1(n):
        return 1

    @staticmethod
    def o_log_n(n):
        return math.log2(n)

    @staticmethod
    def o_n(n):
        return n

    @staticmethod
    def o_n_log_n(n):
        return n * math.log2(n)

    @staticmethod
    def o_n_2(n):
        return n * n

    @staticmethod
    def o_n_2_log_n(n):
        return n * n * math.log2(n)

    fun_to_string_mapper = [(o_1, "o1"), (o_log_n, "ologn"), (o_n, "on"), (o_n_log_n, "onlogn"), (o_n_2, "on2"),
                            (o_n_2_log_n, "on2logn")]

    @staticmethod
    def map_string_to_func(fun_name):
        for fts in FunctionProvider.fun_to_string_mapper:
            if fts[1] == fun_name:
                return fts[0]
        raise NoSuchFunctionException("No such function for approximation")

    @staticmethod
    def wrap_for_newton_formula(fun, n, given_time):
        return fun(n) - given_time


class NoSuchFunctionException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Task:
    def_init = 'import random; data=[randint(0,__N__) for i in range(__N__)]'
    def_invoke = 'sorted(data)'

    def __init__(this, ini, inv, clr):
        this.ini = ini
        this.inv = inv
        this.clr = clr
