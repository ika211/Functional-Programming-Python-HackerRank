import itertools


def f(delim, arr):
    return filter(lambda a: a < delim, arr)


if __name__ == "__main__":
    X = int(input())
    B = int(input())
    inputArray = [0] * B
    for i in range(B):
        inputArray[i] = int(input())

    result = list(f(X, inputArray))
    print(result)
