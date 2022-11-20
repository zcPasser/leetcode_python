

class Solution:
    def isHappy(self, n: int) -> bool:
        pool = set()
        temp = n
        while True:
            if temp == 1:
                return True
            elif temp in pool:
                return False
            else:
                pool.add(temp)

            digits = []
            while temp > 0:
                digits.append(temp % 10)
                temp = temp // 10
            temp = sum(map(lambda x: x * x, digits))


n = 19
s = Solution()
print(s.isHappy(n))