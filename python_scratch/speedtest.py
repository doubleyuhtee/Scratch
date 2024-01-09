import timeit


def while_loop(n=100_000_000):
    s = 0
    i = 0
    while i < n:
        s += i
        i += 1
    print(2)


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    print(s)


def sum_range(n=100_000_000):
    s = sum(range(n))
    print(s)


def calc(n=100_000_000):
    # summing to n-1 so it's not the exact formula you're used to
    print((n*(n-1))//2)

if __name__ == "__main__":
    print("while loop\t\t", timeit.timeit(while_loop, number=1))
    print("for loop\t\t", timeit.timeit(for_loop, number=1))
    print("listy loop\t\t", timeit.timeit(sum_range, number=1))
    print("calculation\t\t", timeit.timeit(calc, number=1))
