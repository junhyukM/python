def fib_for(n):
    result = [1, 1]
    for i in range(1, n):
        end1 = result[-1]
        end2 = result[len(result) - 2]
        fib_num = end1 + end2
        result.append(fib_num)

    return result[-1]


def fib_re(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib_re(n-1) + fib_re(n-2)