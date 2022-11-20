
'''
    leetcode-1002-查找公共字符串
'''

'''
    思路：
        1、通过字典结构，将1个字符串中字符进行统计，1个字符串对应1个字典。
        2、对每个字符串同样处理。
        2、比较dict_1、dict_2，找出公共key，然后将对应value小的存入dict_3，得到对应字符串的公共串。
        3、按照step2，进行迭代。
'''
def commonChars(words):
    num_words = len(words)
    # 边界考虑
    # 由于题意限制，实则不会出现。
    # if num_words <= 1:
    #     return

    # 将字符串str 通过 字典 统计
    def str2dict(str):
        dict_ = {}
        for s in str:
            dict_[s] = dict_.get(s, 0) + 1

        return dict_

    dicts_list = []
    for str in words:
        dicts_list.append(str2dict(str))

    # 比较2个字典的 公共键 部分
    # 即获取对应2个字符串 的 公共字符
    def get_common_chars(dict_1, dict_2):
        # if len(dict_1)  or
        result_dict = {}
        for k1 in dict_1.keys():
            # 存在 公共字符
            if k1 in dict_2.keys():
                # 获取 最小长度
                result_dict[k1] = min(dict_1[k1], dict_2[k1])

        return result_dict
    # 存放一次公共字符
    result_dict = dicts_list[0]
    for i in range(num_words):
        result_dict = get_common_chars(dicts_list[i], result_dict)

    result_list = []
    # 将 公共字符 结合 次数 放入 列表
    for common_char in result_dict.keys():
        for i in range(result_dict[common_char]):
            result_list.append(common_char)
    return result_list

if __name__ == '__main__':
    words_list = ["bella", "label", "roller"]
    print(commonChars(words_list))