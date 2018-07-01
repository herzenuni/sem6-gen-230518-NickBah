def fib(count):
    lst = [0,1]
    i = 2
    while True:
        result = lst[i - 2] + lst[i - 1]
        lst.append(result)
        i += 1
        if (i == count + 3):
            break
        yield result

g = fib(6)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



