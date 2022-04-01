def f(arr):
    return list(map(lambda tup: tup[1], filter(lambda tup: tup[0] % 2 == 1, enumerate(arr))))


if __name__ == "__main__":
    inputArray = []
    while True:
        temp = input()
        if temp:
            inputArray.append(int(temp))
        else:
            break

    result = f(inputArray)
    print(result)
