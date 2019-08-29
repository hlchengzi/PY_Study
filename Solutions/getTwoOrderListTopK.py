def getTwoOrderListTopK(left, right, k):
    leftCount = 0
    rightCount = 0
    if k < 1:
        return None
    if len(left) + len(right) < k:
        return None
    if len(left) + len(right) == k:
        return left[len(left) - 1] if left[len(left) - 1] > right[len(right) - 1] else right[len(right) - 1]
    while leftCount + rightCount < k - 1:
        if left[leftCount] < right[rightCount]:
            leftCount += 1
        else:
            rightCount += 1
    return right[rightCount] if left[leftCount] > right[rightCount] else left[leftCount]


if __name__ == '__main__':
    left = [1, 2, 5, 7, 5, 7, 9, 11]
    right = [2, 4, 6, 8, 10]
    # swap(right,2,4)
    for i in range(15):
        result = getTwoOrderListTopK(left, right, i)
        print(result)