import numpy


def calculate_expression(a: float, b: float) -> float:
    return 1/(numpy.tan(numpy.pi/4 - 1)**4) + (a*1.5)**(1/3) - b/numpy.arcsin(numpy.mod(a)**2)


def numpy_ex() -> None:
    while True:
        y = 0
        try:
            y = calculate_expression(float(input("Введите a: ")), float(input("Введите b: ")))
        except (TypeError, ValueError):
            print("Неверный ввод, повторите попытку: ")
            continue
        print(f"y в выражении 1.1 равен: {y}")


