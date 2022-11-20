

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r - l) // 2 + l
            square_mid = mid * mid
            if square_mid == x:
                return mid
            elif square_mid < x:
                l = mid + 1
            else:
                r = mid - 1

        return r


x = 14
s = Solution()
print(s.mySqrt(x))

