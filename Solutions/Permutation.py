'''
全排列
'''


def Permutation(ss):
    if not isinstance(ss, str):
        return None
    if len(ss) > 9:
        return None
    if not ss.isalpha():
        return None
    lists = list(set(ss))

    full_permutation(lists, 0, len(lists) - 1)


def full_permutation(lists, begin, end):
    if begin == end:
        global staticCount
        staticCount += 1
        return
    else:
        for i in range(begin, end):
            if is_swap(lists, begin, i):
                swap(lists, begin, i)
                full_permutation(lists, begin + 1, end)
                swap(lists, begin, i)


def swap(lists, a, b):
    lists[a], lists[b] = lists[b], lists[a]


def is_swap(lists, begin, end):
    for i in range(begin + 1, end):
        if lists[begin] == lists[i]:
            return False
    return True