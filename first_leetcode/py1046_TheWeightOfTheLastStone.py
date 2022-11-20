'''
    leetcode-1046-the weight of the last stone
'''

'''
    思路：
        1、
'''

def lastStoneWeight(stones:list):
    if not stones:
        return 0
    while len(stones) > 1:
        x = max(stones)
        stones.remove(x)
        y = max(stones)
        stones.remove(y)
        if x != y:
            stones.append(abs(x - y))

    return 0 if len(stones) == 0 else stones[0]

if __name__ == '__main__':
    pass