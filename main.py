import matplotlib_ex
import numpy_ex
import pandas_ex


def main() -> None:
    while True:
        print("Лабораторная работа #5:\n"
              "1. NumPy\n"
              "2. Pandas\n"
              "3. Matplotlib\n")
        choice = 0
        while True:
            try:
                choice = int(input("Ввод: "))
                break
            except (TypeError, ValueError):
                print("Неверный ввод, повторите попытку: ")
                continue
        if choice == 0:
            break
        elif choice == 1:
            numpy_ex.numpy_ex()
        elif choice == 2:
            pandas_ex.pandas_ex()
        elif choice == 3:
            matplotlib_ex.matplotlib_ex()


main()
