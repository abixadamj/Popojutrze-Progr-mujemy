# Definiowanie funkcji w Python a34
some_value = 20


def function_name():
    print("This is a sample function printing some text.")
    value = 4 * some_value
    print(f"And printing some value = {value}.")


def function_name_other(first_param, second_param):
    return first_param + second_param


def function_returns_tuple(param):
    value_1 = some_value * param
    value_2 = some_value + param
    return value_1, value_2


function_name()
function_name_other(1, 2)
function_returns_tuple(3)

# wywołanie z przepisaniem
ret_value = function_name()
print(ret_value)
ret_value = function_name_other(1, 2)
print(ret_value)
ret_value = function_returns_tuple(3)
print(ret_value)
