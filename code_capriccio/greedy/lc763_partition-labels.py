class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        char_to_idx = [0] * 27
        len_s = len(s)
        for i in range(len_s):
            char_to_idx[ord(s[i]) - ord('a')] = i
        ans = []
        right = 0
        left = 0
        for i in range(len_s):
            # 找到字符出现的最远边界
            right = max(right, char_to_idx[ord(s[i]) - ord('a')])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans
