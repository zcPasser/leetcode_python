
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (r - l) // 2 + l
            y = num / mid

            if y > mid:
                l = mid + 1
            elif y < mid:
                r = mid - 1
            else:
                return True
        return False

x = 1
s = Solution()
print(s.isPerfectSquare(x))