class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr, i, j = len(arr), 0, 0
        while j < len_arr:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        i -= 1
        j -= 1
        while i >= 0:
            if j < len_arr:
                arr[j] = arr[i]
            if arr[i] == 0 and 1 <= j:
                j -= 1
                arr[j] = 0

            i -= 1
            j -= 1
        # idx = 0
        # while idx < len(arr):
        #     if arr[idx] == 0:
        #         arr.pop()
        #         arr.insert(idx + 1, 0)
        #         idx += 2
        #     else:
        #         idx += 1


nums = [1,0,2,3,0,4,5,0]
print(nums)
s = Solution()
s.duplicateZeros(nums)
print(nums)
