from fun_helpers import FunctionProvider
import numpy


class ComplexityCalculator:
    def __init__(self, table_of_times, b):
        self.table_of_times = table_of_times
        self.b = b
        self.function = ""
        self.measures_fit = {"o1": 0, "ologn": 0, "on": 0, "onlogn": 0, "on2": 0, "on2logn": 0}

    def set_function(self, function):
        self.function = function

    def check_max(self):
        minn = -1
        helper_min = -2
        min_phrase = "none"
        helper_min_phrase = "none"
        for tpl in self.measures_fit:
            if tpl[1] > min:
                minn = tpl[1]
                min_phrase = tpl[0]
            elif tpl[1] == min:
                helper_min_phrase = tpl[0]
                helper_min = tpl[0]
        if minn == helper_min:
            print("function between: " + min_phrase + "and" + helper_min_phrase)
            self.set_function(helper_min_phrase)
        else:
            print("complexity of this function is: " + min_phrase)
            self.set_function(min_phrase)

    def check_what_fits(self, tn1, tn2, b):
        lefty = abs(tn2[1] - b) / (tn1[1] - b)
        eps = float("inf")
        to_ret = "loool"
        for i in FunctionProvider.fun_to_string_mapper:
            x = abs(i[0](tn2[0]) / i[0](tn1[0]) - lefty)
            if x <= eps:
                eps = x
                to_ret = i[1]
        return to_ret

    def eval_times(self):
        for i in range(0, len(self.table_of_times) - 1):
            for j in range(i + 1, len(self.table_of_times)):
                to_compare = self.check_what_fits(self.table_of_times[i], self.table_of_times[j], self.b)
                self.measures_fit[to_compare] += 1

        self.check_max()

    def time_for_given_n(self, given_n):
        x_ax = []
        y_ax = []
        fun = FunctionProvider.map_string_to_func(self.function)
        for time in self.table_of_times:
            x_ax.append(fun(time[0]))
            y_ax.append(time[1])
        p = numpy.polyfit(x_ax, y_ax, 1)
        return numpy.polyval(p, fun(given_n))

    def reversed_function(self):
        if self.function == "o1":
            x = [self.table_of_times[i][1] for i in range(len(self.table_of_times))]
            y = [self.table_of_times[i][0] for i in range(len(self.table_of_times))]
            return numpy.polyfit(x, y, 0)
        elif self.function == "on":
            x = [self.table_of_times[i][1] for i in range(len(self.table_of_times))]
            y = [self.table_of_times[i][0] for i in range(len(self.table_of_times))]
            return numpy.polyfit(x, y, 1)
        if self.function == "on2":
            x = [self.table_of_times[i][1] for i in range(len(self.table_of_times))]
            y = [self.table_of_times[i][0] for i in range(len(self.table_of_times))]
            return numpy.polyfit(x, y, 2)

    def n_for_given_time(self, time):
        if self.function == "o1" or self.function == "on" or self.function == "on2":
            p = self.reversed_function()
            return numpy.polyval(p, time)
        else:
            f = FunctionProvider.wrap_for_newton_formula(FunctionProvider.map_string_to_func(self.function), time)
            n = 1
            n2 = 0
            while abs(n - n2) < 10e-3:
                n2 = n
                n = n2 - f(n2)
            return n
