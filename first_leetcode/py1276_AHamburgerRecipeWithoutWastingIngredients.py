'''
    leetcode-1276-A hamburger recipe without wasting ingredients
'''

'''
    思路：
        1、边界：tomatoSlices > cheeseSlices。
        2、数学方程组。
        3、转为整除问题。
'''


def numOfBurgers(tomatoSlices, cheeseSlices):
    # 边界
    if tomatoSlices < cheeseSlices or tomatoSlices < 0:
        return []
    div1, mod1 = divmod(tomatoSlices - 2 * cheeseSlices, 2)
    div2, mod2 = divmod(4 * cheeseSlices - tomatoSlices, 2)
    if mod1 == mod2 == 0 and div1 >= 0 and div2 >= 0:
        return [div1, div2]
    return []