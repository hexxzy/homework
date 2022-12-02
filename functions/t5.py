def fib():
    x1 = x2 = 1
    print(0, x1, x2, end=' ')

    while x1 + x2 < 100:
        x1, x2 = x2, x1 + x2
        print(x2, end=' ')


fib()


def fib(lst = [0,1], a = 0 , b = 1):
    i = len(lst)
    b = lst[i - 1]
    a = lst[i - 2]
    c = a + b
    lst.append(c)
    if b >= 50:
        print(lst)
        return
    else: fib(lst, a , b)
    return lst


fib()