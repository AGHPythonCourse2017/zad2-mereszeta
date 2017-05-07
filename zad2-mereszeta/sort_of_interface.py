import logging

from .calculations import ComplexityCalculator, ComplexityNotCalculatedException
from .timer_related_functions import TimingProvider


class TimerInterface:
    def __init__(self, ini_name, inv_name, clr_name, ttime):
        logging.basicConfig(filename='timerInterface.log', level=logging.DEBUG)
        logging.info('started working with code files')
        self.t_provider = TimingProvider(ini_name, inv_name, clr_name)
        times = self.t_provider.measure_times(ttime)
        b = self.t_provider.provide_b(ttime)
        self.calculator = ComplexityCalculator(times, b)
        logging.info('stopped working with code files')

    def calculate_complexity(self, ttime):
        self.calculator.eval_times()

    def approximate_time(self, n):
        if self.calculator.function == "":
            raise ComplexityNotCalculatedException("You have to calculate complexity first, then approximate time!")
        ttime = self.calculator.time_for_given_n(n)
        print("your function would take aproximately " + str(ttime) + " for given n " + str(n))
        return ttime

    def approximate_range(self, ttime):
        if self.calculator.function == "":
            raise ComplexityNotCalculatedException("You have to calculate complexity first, then approximate time!")
        n = self.calculator.n_for_given_time(ttime)
        print("You can handle a data structure of length:" + str(n) + " for given time: " + str(ttime))
        return n



if __name__ == "__main__":
    main()
