def binary_search(arr, target):
    # Here you write your solution
    # Здесь вы пишите своё решение

    return -1


if __name__ == "__main__":
    # Everything here executes on `python main.py`, not on `pytest`
    # Нижележащие строчки выполняються только по команде `python main.py`, не `pytest`
    my_arr = [1, 2, 4, 55, 451]
    my_target = 4

    result = binary_search(my_arr, my_target)

    print("Array is ", my_arr)
    print("Target is ", my_target)
    print("Result is", result)
    print("Is result equal to target?: " + str(result == 2))
    print("So, your algorithm is", "valid" if result == 2 else "invalid", "(for now)")

