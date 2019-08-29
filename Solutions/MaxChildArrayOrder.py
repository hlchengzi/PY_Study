'''
最长递增子序列LIS
'''


def MaxChildArrayOrder(lists):
    if len(lists) == 0 and lists is None:
        return None
    temp = [1 for i in range(len(lists))]
    for i in range(len(lists)):
        if not isinstance(lists[i], int):
            return None
        for j in range(0, i):
            if lists[i]>lists[j] and temp[j]+1 >temp[j]:
                temp[i] = temp[j]+1
    print(temp)
    return max(temp)

if __name__ == '__main__':
    lists = [1, 2, 5, 7, 5, 7, 9, 11]
    print(MaxChildArrayOrder(lists))