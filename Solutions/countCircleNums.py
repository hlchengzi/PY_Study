"""
美团一面
m*n里面有多少个内切圆
"""


def coutCircleNums(self, M, N):
    if not isinstance(M, int) or not isinstance(N, int):
        return None
    result = countCircle(M, N)
    return result


def countCircle(M, N):
    if M == 1:
        return N
    else:
        need = countCircle(M-1, N) + function1(M, N)
        return need


def function1(m, n):
    nums = 0
    if m >= n:
        for i in range(1,n+1):
            nums += i
    else:
        for j in range(m, n+1):
            nums += j
    return nums


if __name__ == 'main':
    nums = coutCircleNums(55, 900)
    print("nums：" + str(nums))