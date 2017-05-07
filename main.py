from random import randint
from timeit import timeit
import multiprocessing
import time
import numpy
import functools
import math





def o1(n):
    return 1


def ologn(n):
    return math.log2(n)



def on(n):
    return n


def onlogn(n):
    return n * math.log2(n)


def on2(n):
    return n * n


def on2logn(n):
    return n * n * math.log2(n)


def qsor(lst):
    lst.sort()


def init(N):
    lst = []
    for i in range(0, N):
        lst.append(randint(0, N))
    return lst


def timer(to_time, base_name, val, res_q):
    res_q.put(timeit(functools.partial(to_time, val), setup="from __main__ import " + base_name, number=10))


def wrap_timer(to_wait, to_time, base_name, val):
    res_q = multiprocessing.Queue()

    p = multiprocessing.Process(target=timer, name="timer", args=(to_time, base_name, val, res_q))
    p.start()
    time.sleep(to_wait)
    p.join(to_wait)
    if p.is_alive():
        print("data to big to evaluate")
        p.terminate()
        p.join()
        return -1
    else:
        p.join()
        ttime = res_q.get()
        return ttime


def check_max(list_of_tuples):
    min = -1
    helper_min = -2
    min_phrase = "none"
    helper_min_phrase = "none"
    for tpl in list_of_tuples:
        if tpl[1] > min:
            min = tpl[1]
            min_phrase = tpl[0]
        elif tpl[1] == min:
            helper_min_phrase = tpl[0]
            helper_min = tpl[0]
    if min == helper_min:
        print("function between: " + min_phrase + "and" + helper_min_phrase)
    else:
        print("complexity of this function is: " + min_phrase)


def eval_times(time):
    table_of_times = []
    n = 10000
    lst = init(n)
    tt = wrap_timer(time, qsor, "qsor", lst)
    cnt = 0
    lst_b = []
    b = wrap_timer(time, qsor, "qsor", lst_b)
    while tt != -1 and cnt != 5:
        table_of_times.append((n, tt))
        n *= 10
        lst = init(n)
        cnt += 1
        tt = wrap_timer(time, qsor, "qsor", lst)
    if cnt != 5:
        print(n)
        n /= 10
        while cnt != 5:
            new_n = randint(10, n)
            lst = init(new_n)
            tt = wrap_timer(time, qsor, "qsor", lst)
            if tt != -1:
                table_of_times.append((new_n, tt))
                cnt += 1
    measures_fit = [("o1", 0), ("ologn", 0), ("on", 0), ("onlogn", 0), ("on2", 0), ("on2logn", 0)]
    print(len(table_of_times))
    for i in range(0, cnt - 1):
        for j in range(i + 1, cnt):
            to_compare = check_what_fits(table_of_times[i], table_of_times[j], b)
            for measure in measures_fit:
                if measure[0] == to_compare:
                    new = (measure[0], measure[1] + 1)
                    k = measures_fit.index(measure)
                    measures_fit.insert(k, new)
                    break

    check_max(measures_fit)


def check_what_fits(tn1, tn2, b):
    lefty = abs(tn2[1] - b) / (tn1[1] - b)
    measures_fit = [(o1, "o1"), (ologn, "ologn"), (on, "on"), (onlogn, "onlogn"), (on2, "on2"), (on2logn, "on2logn")]
    eps = float("inf")
    to_ret = "loool"
    for i in measures_fit:
        x = abs(i[0](tn2[0]) / i[0](tn1[0]) - lefty)
        if x <= eps:
            eps = x
            to_ret = i[1]
    return to_ret


def time_for_given_n(table_of_times,fun,given_n):
    x_ax=[]
    y_ax=[]
    for time in table_of_times:
        x_ax.append(fun(time[0]))
        y_ax.append(time[1])

    p=numpy.polyfit(x_ax,y_ax,1)
    return numpy.polyval(p,given_n)
def newton_based_func(func,given_time,n):
    return func(n)-given_time

def n_for_given_time(table_of_times,fun,der_fun,given_time):


















def main():
    eval_times(10)


if __name__ == "__main__":
    main()
