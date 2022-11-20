"""
1、有两种特殊字符：
    第一种字符可以用一比特 0 表示
    第二种字符可以用两比特（10 或 11）表示
2、一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。

返回：
    根据bits数组的解码结构最后一个是否一比特字符则返回true、false。
"""


class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        len_of_bits = len(bits)
        i = len_of_bits - 2
        while i >= 0 and bits[i]:
            i -= 1

        return (len_of_bits - i) % 2 == 0
        # i = 0
        # while i < len_of_bits - 1:
        #     i += bits[i] + 1
        #
        # return i == len_of_bits - 1
