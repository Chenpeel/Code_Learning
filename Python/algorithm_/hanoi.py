# hanoi calculate 汉诺塔问题
def hanoi(n: int, a: int, b: int, c: int) -> None:
    if hanoi_calcu(n) > 1000000000:
        print("Too BIG only the times: {}".format(hanoi_calcu(n)))
        return
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving %s to %s" % (a, c))
        hanoi(n-1, b, a, c)


def hanoi_calcu(n:int) -> int:
    return 2**n - 1


n = eval(input())
hanoi(n, "A", "B", "C")
