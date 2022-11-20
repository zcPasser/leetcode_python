# a = [[],[]]
# print(a[:][0])
# print(min((op[0] for op in a)), min((op[1] for op in a)))
import collections
import time


from collections import Counter

a = [1, 2 , 3]
# print(Counter('abcdeabcdjojab').most_common(1)[0][1])

# s_bin = []
# for i in range(0, 128):
#     s = bin(i)[2:]
#     l = len(s)
#     if l < 7:
#         s = '0' * (7 - l) + s
#         # print(s)
#     s_bin.append(s)
#
# cnt = 0
#
#
# def cnt_one(s):
#     cnt = 0
#     for ch in s:
#         if ch == '1':
#             cnt += 1
#     return cnt
#
#
# cnt_of_one = [[], [], [], [], [], [], [], []]
#
# for s in s_bin:
#     if '101' in s and '11'in s:
#         cnt += 1
#         cur_cnt = cnt_one(s)
#         cnt_of_one[cur_cnt].append(s)
        # print(s)
# s = [1, 2]
# print(''.join(s))
# for i in range(8):
#     print('{0}个1：{1}'.format(i, cnt_of_one[i]))
#     print('{0}个1个数：{1}'.format(i, len(cnt_of_one[i])))

# def get_processed_str(s: str) -> str:
#     len_s = len(s)
#     ans = []
#     fast_idx, slow_idx = 0, len_s - 1
#     while fast_idx < len_s:
#         if s[fast_idx] == '#':
#             if ans:
#                 ans.pop()
#         else:
#             ans.append(s[fast_idx])
#         fast_idx += 1
#     return str(ans)
#
# s = "ab##"
# print(get_processed_str(s))
s = [0] * 26
print(-132 // 6)

# a = collections.defaultdict()
# a[-1] += 1
# print(a)

# a = ['abew', 'oschna']
# a[0] = a[0] ^ a[1]
# a[1] = a[0] ^ a[1]
# a[0] = a[0] ^ a[1]
# print(a)