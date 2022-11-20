'''
    leetcode-168-Excel表列名称
'''

'''
    思路：
        1、本质上是10进制 转为 26进制数。
        2、区别：26进制 从1开始。
        3、采用字典存储该26进制信息。
'''


def convertToTitle(columnNumber):
    base_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G',
                 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N',
                 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T',
                 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
    res = ''

    while columnNumber > 0:
        columnNumber -= 1
        div, mod = divmod(columnNumber, 26)
        columnNumber = div
        # if mod
        res = base_dict[mod] + res

    return res

if __name__ == '__main__':
    print(convertToTitle(701))