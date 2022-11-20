"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        n_set.add(n)

        while True:
            # 取出各位数 并 计算其平方和。
            temp_n = 0
            while n != 0:
                num = n % 10
                temp_n += num * num
                n //= 10
            # 边界判定。
            # 成功。
            if temp_n == 1:
                return True
            # 无限循环。
            if temp_n in n_set:
                return False
            # 循环继续。
            n = temp_n
            n_set.add(temp_n)


ss = Solution()
print(ss.isHappy(19))
