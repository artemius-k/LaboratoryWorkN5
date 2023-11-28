import numpy


def calculate_expression(a=0.3, b=-21.17) -> float:
    abs_a = numpy.power(numpy.fabs(a), 2)
    return (numpy.power((1/numpy.tan(numpy.pi/4 - 1)), 4)
            + numpy.power(a+1.5, 1/3)
            - b/numpy.arcsin(abs_a))


def numpy_ex() -> None:
    while True:
        y = 0
        while True:
            try:
                y = calculate_expression()
                break
            except (TypeError, ValueError) as e:
                print(f"{e}")
                print("Неверный ввод, повторите попытку: ")
                continue
        print(f"y в выражении 1.1 равен: {y}")
        break
