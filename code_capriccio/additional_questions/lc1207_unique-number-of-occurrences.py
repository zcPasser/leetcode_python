class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        len_arr = len(arr)
        cnt = [0] * 2002
        for i in range(len_arr):
            cnt[arr[i] + 1000] += 1
        fre = [False] * 1001
        for i in cnt:
            if i > 0:
                if fre[i]:
                    return False
                else:
                    fre[i] = True
        return True