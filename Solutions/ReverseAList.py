def f(list_input):
    return reversed(list_input)


if __name__ == '__main__':
    inp = []
    while True:
        temp = input()
        if temp == "":
            break
        inp.append(int(temp))
    print(*f(inp), sep="\n")

