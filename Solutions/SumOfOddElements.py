from functools import reduce


def f(arr):
    return reduce(lambda a, b: a+b, filter(lambda num: num % 2 != 0, arr))


if __name__ == '__main__':
    input_array = []
    while True:
        temp = input()
        if temp == "":
            break
        input_array.append(int(temp))

    result = f(input_array)
    print("Sum of Odd Elements is :", result)
