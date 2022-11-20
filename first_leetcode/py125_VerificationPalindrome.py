'''
    leetcode-125-verification palindrome
'''


def isPalindrome(s):
    # 整理 有效串
    # 大小写调整
    s = s.lower()
    ss = ''.join([ch for ch in s if 'a' <= ch <= 'z' or '0' <= ch <= '9'])

    # 边界：空 或 单字符
    len_ss = len(ss)
    if len_ss < 2:
        return True

    i, j = 0, len(ss) - 1
    while i < j:
        if ss[i] != ss[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    print(ord('0'))
    print(ord('0'))
    print(ord('O'))
    print(isPalindrome("0P"))