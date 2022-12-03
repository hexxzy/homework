def count(i):
    if i == 10:
        print(i)
    else:
        print(i)
        return count(i + 1)


count(0)