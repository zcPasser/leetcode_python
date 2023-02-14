class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        len_arr = len(arr)
        if len_arr < 3:
            return False
        left, right = 0, len_arr - 1
        while (left < len_arr - 1) and (arr[left] < arr[left + 1]):
            left += 1
        while (right > 0) and (arr[right] < arr[right - 1]):
            right -= 1
        if left == right and left != 0 and right != (len_arr - 1):
            return True
        return False