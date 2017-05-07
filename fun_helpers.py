import math


class FunctionProvider:
    @staticmethod
    def o_1(n):
        return 1

    @staticmethod
    def o_log_n(n):
        return math.log2(n)

    @staticmethod
    def o_log_n_derivative(n):
        return 1 / n

    @staticmethod
    def o_n(n):
        return n

    @staticmethod
    def o_n_log_n(n):
        return n * math.log2(n)

    @staticmethod
    def o_n_log_n_derivative(n):
        return math.log2(n) + 1

    @staticmethod
    def o_n_2(n):
        return n * n

    @staticmethod
    def o_n_2_log_n(n):
        return n * n * math.log2(n)

    @staticmethod
    def o_n_2_log_n_derivative(n):
        return 2 * n * math.log2(n) + n

    fun_to_string_mapper = [(o_1, "o1"), (o_log_n, "ologn"), (o_n, "on"), (o_n_log_n, "onlogn"), (o_n_2, "on2"),
                            (o_n_2_log_n, "on2logn")]

    fun_to_derivative_mapper = [(o_log_n, o_log_n_derivative), (o_n_log_n, o_n_log_n_derivative),
                                (o_n_2_log_n, o_n_2_log_n_derivative)]

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
        return (fun - given_time) / FunctionProvider.map_fun_to_derivative(fun)


class NoSuchFunctionException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Task:
    def_init = 'import random; data=[randint(0,__N__) for i in range(__N__)]'
    def_invoke = 'sorted(data)'

    def __init__(self, ini_name,inv_name,clr_name):
        self.ini_name =ini_name
        self.inv_name=inv_name
        self.clr_name=clr_name

    def open_ini(self):
        f=open(self.ini_name)
        to_ret=f.read()
        f.close()
        return to_ret
    def open_inv(self):
        f=open(self.inv_name)
        to_ret=f.read()
        f.close()
        return to_ret
    def open_clr(self):
        f=open(self.clr_name)
        to_ret=f.read()
        f.close()
        return to_ret

