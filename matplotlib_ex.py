import matplotlib
import numpy
import pylab


def calculate_s(t: float):
    return numpy.emath.log(numpy.fabs(1.3+t)) - numpy.power(numpy.e, t)


def matplotlib_ex():
    t_values = numpy.arange(2, 3, 0.03, dtype=float)
    s_values = numpy.array([calculate_s(t) for t in t_values])

    max_s = numpy.max(s_values)
    average_s = numpy.average(s_values)
    min_s = numpy.min(s_values)

    print("s = ln|1,3 - t| - power(e, t),   2 <= t <= 3,   delta_t = 0,03:\n"
          f"s_values = \n{s_values}\n\n"
          f"s_values_sorted = \n{numpy.sort(s_values)}\n\n"
          f"s_max = {max_s}\n"
          f"s_average = {average_s}\n"
          f"s_min = {min_s}\n"
          f"Количество элементов: {numpy.size(s_values)}\n"
          f"")
