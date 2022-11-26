nechet, chet = 0, 0
def count(i):
    if i == 10:
        chet += 1
        print(i)
    else:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1
        print(i)
        return count(i + 1)
count(0)

print(chet, nechet)