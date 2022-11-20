

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        len_of_arr = len(arr)
        if len_of_arr < 3:
            return False
        left, right = 0, len_of_arr - 1
        while left < len_of_arr - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right >= 1 and arr[right] < arr[right - 1]:
            right -= 1

        return left == right and left != 0 and right != len_of_arr - 1
        # len_of_window = len_of_arr - 1
        # idx = -1
        # while len_of_window >= 1:
        #     if arr[len_of_window - 1] <= arr[len_of_window]:
        #         idx = len_of_window
        #         break
        #     len_of_window -= 1
        #
        # if idx == -1 or idx == len_of_arr - 1:
        #     return False
        #
        # for i in range(0, idx):
        #     if arr[i] >= arr[i + 1]:
        #         return False
        #
        # return True


s = Solution()
arr = [0,1,2,3]
print(s.validMountainArray(arr))