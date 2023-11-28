from matplotlib import pyplot, pylab
import numpy


def calculate_s(t: float):
    return numpy.emath.log(numpy.fabs(1.3+t)) - numpy.power(numpy.e, t)


def exercise_3_1():
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
          f"Количество элементов: {numpy.size(s_values)}\n\n")

    figure, ax = pyplot.subplots()

    ax.axvline(x=0, color="black")
    ax.axhline(y=0, color="black")
    ax.set_xlabel("t")
    ax.set_ylabel("s")

    pyplot.grid(True, which="both")
    lines = ax.plot(t_values, s_values, t_values, [average_s for _ in range(len(t_values))])

    pyplot.setp(lines, linewidth=2.)
    pyplot.setp(lines[0], color="blue")
    pyplot.setp(lines[1], color="orange")

    pyplot.scatter((t_values[0], t_values[-1]), (s_values[0], s_values[-1]), color="blue")
    pyplot.scatter((t_values[0], t_values[-1]), (average_s, average_s), color="orange")

    pyplot.show()


def exercise_3_2():
    x_values = numpy.array([range(0, 10)])
    y_values = numpy.array([range(0, 10)])
    x_values, y_values = pylab.meshgrid(x_values, y_values)

    z_values_1 = calculate_z1(x_values, y_values)
    z_values_2 = calculate_z2(x_values, y_values)
    z_values_3 = calculate_z3(x_values, y_values)
    z_values_4 = calculate_z4(x_values, y_values)
    z_values_5 = calculate_z5(x_values, y_values)

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(x_values, y_values, z_values_1, color="red")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(x_values, y_values, z_values_2, color="orange")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(x_values, y_values, z_values_3, color="yellow")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(x_values, y_values, z_values_4, color="green")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(x_values, y_values, z_values_5, color="blue")

    pyplot.show()


def calculate_z1(x, y):
    return numpy.float_power(x, 0.25) + numpy.float_power(y, 0.25)


def calculate_z2(x, y):
    return x*x - y*y


def calculate_z3(x, y):
    return 2*x + 3*y


def calculate_z4(x, y):
    return x*x + y*y


def calculate_z5(x, y):
    return 2 + 2*x + 2*y - x*x - y*y


def matplotlib_ex():
    exercise_3_1()
    exercise_3_2()
