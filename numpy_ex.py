import numpy
import random


def calculate_expression(a=0.3, b=-21.17) -> None:
    abs_a = numpy.power(numpy.fabs(a), 2)
    y = (numpy.power((1/numpy.tan(numpy.pi/4 - 1)), 4)
            + numpy.power(a+1.5, 1/3)
            - b/numpy.arcsin(abs_a))
    print(f"y в выражении 1.1 равен: {y}")


def calculate_regression_equation_estimation() -> None:
    x = numpy.array(
        [
            [1, random.randint(15, 27), random.randint(60, 82)]
            for _ in range(12)
        ], float
    )
    y = numpy.random.uniform(13.5, 18.6, (12, 1))

    x_t = x.transpose()
    a = numpy.dot(numpy.linalg.inv(numpy.dot(x_t, x)), numpy.dot(x_t, y))
    calculated_y = numpy.array([a[0] + a[1] * x[i, 1] + a[2] * x[i, 2] for i in range(12)])

    print(f"X = \n{x}")
    print(f"Y = \n{y}")
    print(f"A = \n{a}")
    print(f"Y' = \n{calculated_y}")


def numpy_ex() -> None:
    calculate_expression()
    calculate_regression_equation_estimation()
