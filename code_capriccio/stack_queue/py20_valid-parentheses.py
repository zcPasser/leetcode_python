

class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        char_to_char = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in char_to_char.keys():
                stack_list.append(char_to_char[ch])
            elif not stack_list or stack_list[-1] != ch:
                return False
            else:
                stack_list.pop()
        return not stack_list


s = "["
s_ = Solution()
print(s_.isValid(s))