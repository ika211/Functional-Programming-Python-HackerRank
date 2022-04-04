def f(arr: list):
    return sum(map(lambda a: 1, arr))


if __name__ == '__main__':
    input_array = []
    while True:
        temp = input()
        if temp == "":
            break
        input_array.append(int(temp))

    result = f(input_array)
    print("Length of the array is:", result)