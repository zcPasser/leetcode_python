'''
    leetcode-167-两数之和 II - 输入有序数组
'''
'''
    思路：
        1、
'''


def twoSum(numbers, target):
    hashtable = {}
    for i, v in enumerate(numbers):
        if (target - v) in hashtable.keys():
            return [hashtable[target - v] + 1, i + 1]
        hashtable[v] = i
    return []


