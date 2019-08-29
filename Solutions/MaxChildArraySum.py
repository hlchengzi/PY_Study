def MaxChildArrayOrder(lists):
    if len(lists) == 0:
        return 0
    if lists is None:
        return None
    temp = [0 for i in range(len(lists))]
    temp[0] = lists[0]
    for i in range(1, len(lists)):
        if not isinstance(lists[i], int):
            return None
        temp[i] = max(lists[i] + temp[i - 1], lists[i])
    return max(temp)


if __name__ == '__main__':
    arr = [6, -1, 3, -4, -6, 9, 2, -2, 5]
    print(MaxChildArrayOrder(arr))
