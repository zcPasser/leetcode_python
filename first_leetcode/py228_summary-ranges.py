"""
给定一个 无重复元素 的有序 整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b

"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        str_list = []
        seq_list = []
        for num in nums:
            if not seq_list:
                seq_list.append(num)
            else:
                if num == seq_list[-1] + 1:
                    seq_list.append(num)
                else:
                    if len(seq_list) == 1:
                       str_list.append(str(seq_list[0]))
                    else:
                        str_list.append(str(seq_list[0]) + '->' + str(seq_list[-1]))
                    seq_list = [num]
        if len(seq_list) == 1:
            str_list.append(str(seq_list[0]))
        else:
            str_list.append(str(seq_list[0]) + '->' + str(seq_list[-1]))

        return str_list


nums_list = [0, 2, 3, 4, 6, 8, 9]
ss = Solution()
print(ss.summaryRanges(nums_list))