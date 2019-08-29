'''
python 解决零钱找零问题
'''
import sys

'''
采用递归暴力搜索的方法
'''
def chargedp(lists,total):
    for item in lists:
        if total == item:
            return 1
    minNums = sys.maxsize
    for item in lists:
        if item < total:
            minNums = min(minNums, chargedp(lists,total-item)+1)
    return minNums


'''
采用动态规划的方法
时间复杂度M*N
'''
def charge(lists, total):
    '''
    result为结果构建矩阵，result[i][j]表示使用前i枚类型的硬币的时候对于金额j所需要的最小钱数
    '''
    result = [[0 for i in range(total+1)] for j in range(len(lists)+1)]
    for i in range(len(lists)+1):
        result[i][0] = 0
    for j in range(total+1):
        result[0][j] = sys.maxsize
    for jMoney in range(1, total+1):
        for iCoinKinds in range(1, len(lists)+1):
            '''
            特殊情况2，coinsValues数组下标是从0开始的, result[][]
            数组下标是从1开始计算的
            '''
            if jMoney < lists[iCoinKinds-1]:
                result[iCoinKinds][jMoney] = result[iCoinKinds - 1][jMoney]
                continue

            '''
            对于每个问题，选中其中最小的
            即，判断用不用当前第iCoinKinds类型的硬币和用所使用的
            '''
            if result[iCoinKinds - 1][jMoney] < (result[iCoinKinds][jMoney - lists[iCoinKinds - 1]] + 1):
                result[iCoinKinds][jMoney] = result[iCoinKinds - 1][jMoney]
            else:
                result[iCoinKinds][jMoney] = result[iCoinKinds][jMoney - lists[iCoinKinds - 1]] + 1
    return result[len(lists)][total]



if __name__ == '__main__':
    lists = [1, 2, 4]
    print(chargedp(lists, 8))
    print(charge(lists, 8))
