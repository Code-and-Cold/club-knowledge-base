def sort_the_people(names, heights):
    # Here you write your solution
    # Здесь вы пишите своё решение

    return -1


if __name__ == "__main__":
    # Everything here executes on `python main.py`, not on `pytest`
    # Нижележащие строчки выполняются только по команде `python main.py`, не `pytest`
    names = ["Mary","John","Emma"]
    heights = [180, 165, 170]
    out = ["Mary","Emma","John"]

    result = sort_the_people(names, heights)

    print("Inp is ", names, heights, sep="\n")
    print("Target is ",out)
    print("Result is", result)
    print("Is result equal to target?: ", result == out)
    print("So, your algorithm is", "valid" if result == out else "invalid", "(for now)")
