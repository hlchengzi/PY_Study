"""
    百度面题，获取字符串当中的第一个有序数组下标
    """
def getFirstOrderNums( nums):
    if not isinstance(nums, str):
        return None
    if nums == None and len(nums) < 4:
        return None
    temp = []
    """
    将字符串转化为数组
    """
    lists = list(map(int, list(nums)))
    for i in range(len(lists)):

        if len(temp) == 0:
            if lists[i] == 1:
                temp.append(lists[i])
        else:
            if lists[i] == temp[-1] + 1:
                temp.append(lists[i])
                if len(temp) == 4:
                    return i - 3
            else:
                temp = []
                if lists[i] == 1:
                    temp.append(lists[i])
    return None


if __name__ == 'main':
    index = getFirstOrderNums("12312341234")
    print("index:" + str(index))