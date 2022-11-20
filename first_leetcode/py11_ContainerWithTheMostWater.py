'''
    leetcode-11-container with the most water
'''

'''
    思路：
        1、
'''


def maxArea(height):
    # 暴力法
    # n = len(height)
    # # 边界
    # if n < 2:
    #     return 0
    # lst = [(i, height) for i, height in enumerate(height)]
    #
    # max_area = 0
    #
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         h = min(height[i], height[j])
    #         area = h * (j - i)
    #         max_area = max_area if area < max_area else area
    # return max_area

    # 双指针法
    n = len(height)
    # 边界
    if n < 2:
        return 0
    max_area = 0
    # 从两端移动指针，且每次移动对应 value小 的 指针
    i, j = 0, n - 1
    while i < j:
        max_area = max((j - i) * min(height[i], height[j]), max_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    pass