from timeit import timeit
import multiprocessing
import time
from random import randint
from fun_helpers import Task


class TimingProvider:
    def __init__(self, ini, inv, clr):
        self.mytask = Task(ini, inv, clr)

    def timer(self, res_q, n):
        res_q.put(timeit(self.mytask.inv, setup="n = " + str(n) + ";data = " + self.mytask.inv))

    def wrap_timer(self, to_wait, n):
        res_q = multiprocessing.Queue()

        p = multiprocessing.Process(target=self.timer, name="timer", args=(res_q, n,))
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

    def eval_times(self, ttime):
        table_of_times = []
        n = 10000
        eval(self.mytask.ini, n)
        tt = self.wrap_timer(ttime, n)
        cnt = 0
        b = self.wrap_timer(ttime, 0)
        while tt != -1 and cnt != 5:
            table_of_times.append((n, tt))
            n *= 10
            cnt += 1
            tt = self.wrap_timer(ttime, n)
        if cnt != 5:
            print(n)
            n /= 10
            while cnt != 5:
                new_n = randint(10, n)
                tt = self.wrap_timer(ttime, n)
                if tt != -1:
                    table_of_times.append((new_n, tt))
                    cnt += 1
        return table_of_times
