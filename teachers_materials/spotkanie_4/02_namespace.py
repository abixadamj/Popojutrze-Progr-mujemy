# Funkcje i zasięg zmiennych w Python a35
# główna przestrzeń nazw: "__main__"
some_value = 12
some_list = [1, 2]


def function_1():
    print(some_value)
    print(some_list)


def function_2():
    some_value = "Other value"  # zmienna rodzaju unmutable
    some_list = "Other list"  # zmienna rodzaju unmutable, bo przypisanie innej wartości
    print(some_value)
    print(some_list)


def function_3(param_1, param_2):
    print(f"Parameter 1 value: {param_1}")
    print(f"Parameter 2 value: {param_2}")


def function_4():
    some_list.append(3)  # zmienna rodzaju mutable
    print(some_value)
    print(some_list)


function_1()
function_2()
function_3(some_value, some_list)
function_4()
