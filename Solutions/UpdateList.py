def f(arr: list):
    return list(map(abs, arr))


if __name__ == '__main__':
    input_array = []

    while True:
        temp = input()
        if temp == "":
            break
        input_array.append(int(temp))

    result = f(input_array)
    
    print(*result, sep="\n")