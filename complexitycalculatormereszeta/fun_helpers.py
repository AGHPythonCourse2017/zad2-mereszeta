import math


class FunctionProvider:
    fun_to_string_mapper = [(lambda n: 1, "o1"), (lambda n: math.log2(n), "ologn"), (lambda n: n, "on"),
                            (lambda n: n * math.log2(n), "onlogn"), (lambda n: n * n, "on2"),
                            (lambda n: n * n * math.log2(n), "on2logn")]

    fun_to_derivative_mapper = [(lambda n: math.log2(n), lambda n: 1 / n),
                                (lambda n: n * math.log2(n), lambda n: math.log2(n) + 1),
                                (lambda n: n * n * math.log2(n), lambda n: 2 * n * math.log2(n))]

    @staticmethod
    def ret_list_of_funcs():
        ret = []
        for i in FunctionProvider.fun_to_string_mapper:
            ret.append(i[0])
        return ret

    @staticmethod
    def map_fun_to_derivative(fun):
        for ftdm in FunctionProvider.fun_to_derivative_mapper:
            if ftdm[0] == fun:
                return ftdm[1]
        raise NoSuchFunctionException("no such function!")

    @staticmethod
    def map_string_to_func(fun_name):
        for fts in FunctionProvider.fun_to_string_mapper:
            if fts[1] == fun_name:
                return fts[0]
        raise NoSuchFunctionException("No such function for approximation")

    @staticmethod
    def wrap_for_newton_formula(fun, given_time):
        def wrap_it(n):
            return fun(n)-given_time(n)/FunctionProvider.map_fun_to_derivative(fun)
        return wrap_it


class NoSuchFunctionException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Task:
    def __init__(self, ini_name, inv_name, clr_name):
        self.ini_name = ini_name
        self.inv_name = inv_name
        self.clr_name = clr_name

    def open_ini(self):
        f = open(self.ini_name)
        to_ret = f.read()
        f.close()
        return to_ret

    def open_inv(self):
        f = open(self.inv_name)
        to_ret = f.read()
        f.close()
        return to_ret

    def open_clr(self):
        f = open(self.clr_name)
        to_ret = f.read()
        f.close()
        return to_ret
