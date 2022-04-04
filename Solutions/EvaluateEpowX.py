from itertools import repeat


def fac(num):
    if num < 2:
        return 1
    else:
        return num * fac(num - 1)


def f(X: float) -> float:
    return f2(X, 9)


def f2(X: float, num: int) -> float:
    if num < 1:
        return 1
    else:
        return pow(X, num) / fac(num) + f2(X, num-1)


if __name__ == '__main__':
    N = int(input())
    input_array = []
    for i in range(N):
        input_array.append(float(input()))

    result = list(map(round, map(f, input_array), repeat(4, N)))
    print(*result, sep="\n")